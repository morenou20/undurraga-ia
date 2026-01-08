import pandas as pd


def lluvia_por_periodo(
    df: pd.DataFrame,
    inicio: str,
    fin: str
) -> float:
    """
    Suma lluvia en un periodo fenológico
    """

    mask = (df["fecha"] >= inicio) & (df["fecha"] <= fin)
    return float(df.loc[mask, "precipitacion_mm"].sum())