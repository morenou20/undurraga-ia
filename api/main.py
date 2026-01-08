from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# --------------------
# APP
# --------------------
app = FastAPI(title="Undurraga – Vine Forecast API")

# --------------------
# PATHS
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "forecast_base.pkl"

# --------------------
# LOAD MODEL
# --------------------
model = joblib.load(MODEL_PATH)

# --------------------
# INPUT SCHEMA
# --------------------
class ForecastInput(BaseModel):
    gdd: float
    lluvia_floracion: float
    lluvia_temporada: float
    temp_max_media: float


# --------------------
# ENDPOINT
# --------------------
@app.post("/forecast")
def forecast(data: ForecastInput):
    pred = model.predict([[
        data.gdd,
        data.lluvia_floracion,
        data.lluvia_temporada,
        data.temp_max_media
    ]])

    return {
        "rendimiento_t_ha": round(float(pred[0]), 2),
        "modelo": "xgboost"
    }