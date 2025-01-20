from fastapi import APIRouter, HTTPException, status, Response
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Controllers.medico_controller import ControllerEndpoints_Medico
from typing import List

router = APIRouter(
    prefix="/medicos",
    tags=["Medicos"],
)

# Instancia de la clase ControllerEndpoints
medico_controllers = ControllerEndpoints_Medico()


# Endpoint para obtener la lista de doctores
@router.get("/api")
def Bienvenida():
    return ["BIENVENIDO MY LORD"]


@router.post("/api/medico", status_code=status.HTTP_201_CREATED)
def Registrar_Medico(doctor: MedicoSchema):
    try:
        medico_controllers.Insertar_Medico_Controllers(doctor)
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado: {str(e)}",
        )


@router.get("/api/medico", response_model=List[MedicoSchema])
def Listado_Medicos():
    try:
        listado_total_Medicos = medico_controllers.Listados_Medico_Controllers()
        return listado_total_Medicos

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al obtener el listado de médicos: {str(e)}",
        )


@router.put("/api/medico/{id_medico}", response_model=MedicoSchema)
def Actualizar_Medico(data_medico: MedicoSchema):

    try:
        # Llamar al controlador para actualizar el médico
        respuesta_controllers = medico_controllers.Actualizar_Medico_Controllers(
            data_medico
        )
        return respuesta_controllers
    except HTTPException as http_exc:
        # Repropagar la excepción HTTP
        raise http_exc
    except Exception as e:
        # Manejar cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado al actualizar médico: {str(e)}",
        )


@router.delete("/api/medico/{id_medico}", status_code=status.HTTP_204_NO_CONTENT)
def Eliminar_Medico(id_medico: int):
    try:
        # Llamar al controlador para manejar la eliminación del médico
        medico_controllers.Eliminar_Medico_Controller(id_medico)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException as http_exc:
        # Repropagar HTTPException sin modificarla
        raise http_exc
    except Exception as e:
        # Manejar cualquier otro error inesperado
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado al eliminar médico: {str(e)}",
        )
