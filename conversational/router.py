def route_intent(intent, contexto):
    if intent == "prediccion_rendimiento":
        return "modelo_climatico"
    if intent == "produccion_vino":
        return "modelo_productivo"
    if intent == "escenario_climatico":
        return "simulacion"
    return "respuesta_llm"