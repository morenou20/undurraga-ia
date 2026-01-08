import pandas as pd


def calcular_gdd(
    df: pd.DataFrame,
    base: float = 10.0
) -> pd.DataFrame:
    """
    Calcula Growing Degree Days (GDD)
    """

    df = df.copy()

    df["gdd_dia"] = (
        (df["temp_max"] + df["temp_min"]) / 2 - base
    ).clip(lower=0)

    df["gdd_acumulado"] = df["gdd_dia"].cumsum()

    return df