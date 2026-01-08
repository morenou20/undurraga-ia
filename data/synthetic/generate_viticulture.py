import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

N = 1200  # temporadas

data = {
    "gdd": np.random.normal(1650, 120, N).clip(1300, 1900),
    "rain_flowering": np.random.normal(35, 15, N).clip(5, 90),
    "rain_season": np.random.normal(260, 80, N).clip(80, 500),
    "temp_max_mean": np.random.normal(29, 1.8, N).clip(24, 34),
}

df = pd.DataFrame(data)

# modelo agronómico simplificado para rendimiento
df["yield_t_ha"] = (
    6
    + 0.0025 * df["gdd"]
    - 0.03 * df["rain_flowering"]
    + 0.004 * df["rain_season"]
    - 0.15 * (df["temp_max_mean"] - 28) ** 2
    + np.random.normal(0, 0.6, N)
).clip(4, 14)

# Guardar
BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUT_PATH = BASE_DIR / "data" / "synthetic" / "base_viticulture.csv"

df.round(2).to_csv(OUT_PATH, index=False)
print(f"Dataset generado: {OUT_PATH}")