from pydantic import BaseModel
from typing import Optional

class ContextoProductivo(BaseModel):
    cuartel: Optional[str]
    variedad: Optional[str]
    temporada: Optional[str]
    superficie_ha: Optional[float]

class InputClimatico(BaseModel):
    gdd: Optional[float]
    lluvia_floracion_mm: Optional[float]
    lluvia_temporada_mm: Optional[float]
    temp_max_media: Optional[float]