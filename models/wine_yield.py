# Factores típicos (pueden calibrarse después)
VARIEDAD_FACTORES = {
    "cabernet_sauvignon": 720,
    "carmenere": 700,
    "merlot": 730,
    "syrah": 710,
    "sauvignon_blanc": 750,
    "chardonnay": 760,
}

CUARTEL_FACTORES = {
    "premium": 0.85,
    "estandar": 1.0,
    "alto_rendimiento": 1.15,
}

def estimar_vino_litros(
    rendimiento_t_ha,
    superficie_ha,
    variedad,
    cuartel_tipo
):
    litros_por_ton = VARIEDAD_FACTORES.get(variedad, 720)
    factor_cuartel = CUARTEL_FACTORES.get(cuartel_tipo, 1.0)

    litros = (
        rendimiento_t_ha
        * superficie_ha
        * litros_por_ton
        * factor_cuartel
    )

    return round(litros, 0)