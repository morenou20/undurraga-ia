def responder_prediccion(valor, perfil):
    if perfil == "ejecutivo":
        return f"El rendimiento estimado es cercano a {valor} t/ha, dentro del rango esperado."
    if perfil == "tecnico":
        return f"Según el modelo climático, el rendimiento estimado es {valor} t/ha considerando GDD y precipitación."
    return f"Se espera un rendimiento aproximado de {valor} t/ha."
