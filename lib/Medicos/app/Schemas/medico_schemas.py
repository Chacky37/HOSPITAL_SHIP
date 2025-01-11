from pydantic import BaseModel
from typing import Optional

class MedicoSchema(BaseModel):
    id: int
    name: str
    specialty: Optional[str]
    contraseña: int
