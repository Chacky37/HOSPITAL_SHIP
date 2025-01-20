from pydantic import BaseModel


class PacienteSchema(BaseModel):
    cedula: int
    nombre: str
    edad: int
