import os
from dotenv import load_dotenv
import cdsapi

# --------------------
# Cargar variables del .env
# --------------------
load_dotenv()

url = os.environ.get("URL")
key = os.environ.get("KEY")

if not url or not key:
    raise ValueError("Faltan CDS_URL o CDS_KEY en el .env")

# --------------------
# Cliente CDS con visualizador
# --------------------
c = cdsapi.Client(
    url=url,
    key=key,
    progress=True,   # 👈 barra de progreso
    quiet=False      # 👈 muestra logs
)

# --------------------
# Descarga ERA5
# --------------------
c.retrieve(
    "reanalysis-era5-single-levels",
    {
        "product_type": "reanalysis",
        "variable": [
            "2m_temperature",
            "total_precipitation",
            "surface_solar_radiation_downwards"
        ],
        "year": "2020",
        "month": "01",
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": [f"{h:02d}:00" for h in range(24)],
        "format": "netcdf"
    },
    "era5_chile_central.nc"
)