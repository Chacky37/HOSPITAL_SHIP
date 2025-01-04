from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, HTTPException, status
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Controllers.medico_controller import ControllerEndpoints

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)

# Instancia de la clase ControllerEndpoints
medico_controllers = ControllerEndpoints()

# Endpoint para obtener la lista de doctores
@router.get("/api")
def get_doctors():
    return ["BIENVENIDO MY LORD"]

@router.post("/api/medico")
def Register_Medico(doctor: MedicoSchema):
    try:
        respuesta = medico_controllers.create_doctor(doctor)
        return respuesta
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado: {str(e)}"
        )