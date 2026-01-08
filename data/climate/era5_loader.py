import cdsapi
import xarray as xr
import pandas as pd
from datetime import datetime
import os


def cargar_clima_era5(
    lat: float,
    lon: float,
    fecha_inicio: str,
    fecha_fin: str
) -> pd.DataFrame:
    """
    Descarga clima diario ERA5
    """

    c = cdsapi.Client()

    start = datetime.fromisoformat(fecha_inicio)
    end = datetime.fromisoformat(fecha_fin)

    years = list(range(start.year, end.year + 1))

    file_name = f"era5_{lat}_{lon}.nc"

    if not os.path.exists(file_name):
        c.retrieve(
            "reanalysis-era5-single-levels",
            {
                "product_type": "reanalysis",
                "variable": [
                    "2m_temperature",
                    "total_precipitation"
                ],
                "year": years,
                "month": list(range(1, 13)),
                "day": list(range(1, 32)),
                "time": "12:00",
                "area": [
                    lat + 0.25, lon - 0.25,
                    lat - 0.25, lon + 0.25
                ],
                "format": "netcdf"
            },
            file_name
        )

    ds = xr.open_dataset(file_name)

    df = ds.to_dataframe().reset_index()

    df = df.rename(columns={
        "time": "fecha",
        "t2m": "temp_k",
        "tp": "precipitacion_m"
    })

    df["temp_media"] = df["temp_k"] - 273.15
    df["precipitacion_mm"] = df["precipitacion_m"] * 1000

    return df[["fecha", "temp_media", "precipitacion_mm"]]