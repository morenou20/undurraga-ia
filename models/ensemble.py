import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

xgb_model = joblib.load(BASE_DIR / "models" / "forecast_base.pkl")
prophet_model = joblib.load(BASE_DIR / "models" / "prophet_yield.pkl")

def predict_ensemble(
    grados_dia_crecimiento,
    lluvia_floracion_mm,
    lluvia_temporada_mm,
    temperatura_max_media,
    year
):
    # Modelo climático
    climate_pred = float(
        xgb_model.predict([[
            grados_dia_crecimiento,
            lluvia_floracion_mm,
            lluvia_temporada_mm,
            temperatura_max_media
        ]])[0]
    )

    # Tendencia histórica
    future = pd.DataFrame({
        "ds": pd.to_datetime([f"{year}-12-31"])
    })
    trend_pred = float(prophet_model.predict(future)["yhat"].iloc[0])

    # Ensemble
    final_pred = 0.7 * climate_pred + 0.3 * trend_pred

    return {
        "rendimiento_climatico_t_ha": round(climate_pred, 2),
        "rendimiento_tendencia_t_ha": round(trend_pred, 2),
        "rendimiento_final_t_ha": round(final_pred, 2)
    }