from fastapi import APIRouter, HTTPException, status, Response
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Controllers.medico_controller import ControllerEndpoints
from starlette.status import HTTP_201_CREATED
from typing import List

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

@router.post("/api/medico", status_code=HTTP_201_CREATED )
def Register_Medico(doctor: MedicoSchema):
    try:
        medico_controllers.create_doctor(doctor)
        return Response(status_code=HTTP_201_CREATED)
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado: {str(e)}"
        )
        
@router.get("/api/medico", response_model=List[MedicoSchema])
def Listado_Medicos():
    try:
        listado_total_Medicos = medico_controllers.Listados_doctores()
        return  listado_total_Medicos

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado al obtener el listado de médicos en routers: {str(e)}"
        )
