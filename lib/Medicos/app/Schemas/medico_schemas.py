from pydantic import BaseModel
from typing import Optional


class MedicoSchema(BaseModel):
    Cedula: int
    Primer_Nombre: str
    Segundo_Nombre: Optional[str]
    Primer_Apellido: str
    Segundo_Apellido: Optional[str]
    Especialidad: str
    Contraseña: str
