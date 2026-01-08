import pandas as pd
from prophet import Prophet
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "synthetic" / "base_viticulture.csv"

df = pd.read_csv(DATA_PATH)

# Simular años
# limitar dataset temporal (máx 80 años)
n = len(df)
start_year = 1980
years = min(n, 80)

df = df.iloc[:years].copy()

df["ds"] = pd.date_range(
    start=f"{start_year}-12-31",
    periods=years,
    freq="YE"
)

df["y"] = df["yield_t_ha"]

model = Prophet(
    yearly_seasonality=False,
    changepoint_prior_scale=0.2
)

model.fit(df[["ds", "y"]])

MODEL_PATH = BASE_DIR / "models" / "prophet_yield.pkl"
joblib.dump(model, MODEL_PATH)

print(f"Modelo Prophet guardado en: {MODEL_PATH}")