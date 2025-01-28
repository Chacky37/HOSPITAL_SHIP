from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from lib.Pacientes.app.Schemas.paciente_schemas import PacienteSchema
from lib.Pacientes.app.Controllers.paciente_controller import (
    ControllerEndpoints_Paciente,
)
from typing import List

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"],
)

paciente_controllers = ControllerEndpoints_Paciente()


@router.get("/api")
def Bienvenida():
    return ["BIENVENIDO MY LORD"]


@router.post("/api/paciente", status_code=status.HTTP_201_CREATED)
def Registrar_Paciente(data_paciente: PacienteSchema):
    try:
        paciente_controllers.Insertar_Paciente_Controllers(data_paciente)

        return JSONResponse(
            content={"mensaje": "Paciente registrado exitosamente"},
            status_code=status.HTTP_201_CREATED,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado: {str(e)}",
        )


@router.get("/api/paciente", response_model=List[PacienteSchema])
def Listado_Paciente():
    try:
        listado_total_Pacientes = paciente_controllers.Listados_Paciente_Controllers()
        return listado_total_Pacientes

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al obtener el listado de paciente: {str(e)}",
        )


@router.put("/api/paciente/{id_paciente}", response_model=PacienteSchema)
def Actualizar_Paciente(data_paciente: PacienteSchema):

    try:
        paciente_controllers.Actualizar_Paciente_Controllers(
            data_paciente
        )
        paciente_actualizado = data_paciente.model_dump()
        return JSONResponse(
            content={
                "mensaje": "Paciente actualizado exitosamente",
                "paciente": paciente_actualizado,
            },
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error inesperado al actualizar paciente: {str(e)}",
        )


@router.delete("/api/medico/{id_paciente}", status_code=status.HTTP_200_OK)
def Eliminar_Paciente(id_paciente: int):
    try:
        paciente_controllers.Eliminar_Paciente_Controller(id_paciente)
        return JSONResponse(
            content={"mensaje": "Paciente eliminado exitosamente"},
            status_code=status.HTTP_200_OK,
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al eliminar paciente: {str(e)}",
        )
