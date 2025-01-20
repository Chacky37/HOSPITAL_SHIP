from fastapi import APIRouter, HTTPException, status
from lib.Pacientes.app.Schemas.paciente_schemas import PacienteSchema
from lib.Pacientes.app.Controllers.paciente_controller import ControllerEndpoints

router = APIRouter(
    prefix="/Enfermos",
    tags=["Enfermos"],
)

# Instancia de la clase ControllerEndpoints
medico_controllers = ControllerEndpoints()


# Endpoint para obtener la lista de doctores
@router.get("/api/list")
def get_doctors():
    return ["BIENVENIDO MY LORD PACIENTE"]


@router.post("/api/pacientes")
def Register_Medico(enfermo: PacienteSchema):
    try:
        respuesta = medico_controllers.create_enfermo(enfermo)
        return respuesta
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado: {str(e)}",
        )
