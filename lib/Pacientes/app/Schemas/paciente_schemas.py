from pydantic import BaseModel


class PacienteSchema(BaseModel):
    Cedula: int
    Nombre: str
    Edad: int
