from enum import Enum

class Intent(str, Enum):
    PREDICCION_RENDIMIENTO = "prediccion_rendimiento"
    PRODUCCION_VINO = "produccion_vino"
    ESCENARIO_CLIMATICO = "escenario_climatico"
    ANALISIS_TEMPORADA = "analisis_temporada"
    EXPLICACION_MODELO = "explicacion_modelo"
    CONSULTA_GENERAL = "consulta_general"