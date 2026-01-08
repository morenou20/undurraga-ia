from pathlib import Path
import sys
import joblib
import pandas as pd
import xgboost as xgb

from data.climate.era5_loader import cargar_clima_era5
from features.gdd import calcular_gdd
from features.fenologia import lluvia_por_periodo

# --------------------
# PATHS
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "forecast_base.pkl"

ERA5_PATH = BASE_DIR / "data" / "climate" / "era5.nc"

# --------------------
# PERIODO PRODUCTIVO
# --------------------
FECHA_INICIO = "2018-09-01"
FECHA_FIN = "2023-04-30"

# --------------------
# 1. CARGA CLIMA (ERA5)
# --------------------
if not ERA5_PATH.exists():
    print("❌ No se encontró el archivo ERA5:", ERA5_PATH)
    sys.exit(1)

df_clima = cargar_clima_era5(ERA5_PATH)
print("✅ Clima cargado desde ERA5")

# Filtrar periodo productivo
df_clima["fecha"] = pd.to_datetime(df_clima["fecha"])
df_clima = df_clima[
    (df_clima["fecha"] >= FECHA_INICIO) &
    (df_clima["fecha"] <= FECHA_FIN)
].reset_index(drop=True)

# --------------------
# 2. VALIDACIONES
# --------------------
required_cols = {
    "fecha",
    "temp_media",
    "temp_max",
    "precipitacion"
}

missing = required_cols - set(df_clima.columns)
if missing:
    raise ValueError(f"Faltan columnas climáticas: {missing}")

# --------------------
# 3. FEATURES CLIMÁTICOS
# --------------------
# GDD diario
df_clima["gdd"] = df_clima["temp_media"].apply(calcular_gdd)

gdd_total = df_clima["gdd"].sum()

# Lluvia por periodo fenológico (ejemplo floración)
lluvia_floracion = lluvia_por_periodo(
    df_clima,
    inicio="2018-10-01",
    fin="2018-11-15"
)

lluvia_temporada = df_clima["precipitacion"].sum()

temp_max_media = df_clima["temp_max"].mean()

# --------------------
# 4. DATASET DE ENTRENAMIENTO
# --------------------
# ⚠️ Placeholder: en producción vendrá del histórico real de la viña
X = pd.DataFrame([{
    "gdd": gdd_total,
    "lluvia_floracion": lluvia_floracion,
    "lluvia_temporada": lluvia_temporada,
    "temp_max_media": temp_max_media
}])

# Rendimiento histórico real (ejemplo)
y = pd.Series([9.8])  # toneladas por hectárea

# --------------------
# 5. ENTRENAMIENTO MODELO
# --------------------
model = xgb.XGBRegressor(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X, y)

# --------------------
# 6. GUARDAR MODELO
# --------------------
joblib.dump(model, MODEL_PATH)

print("✅ Modelo entrenado correctamente")
print("📦 Guardado en:", MODEL_PATH)