from fastapi import APIRouter

router = APIRouter(
    prefix="/specialities",
    tags=["Specialities"],
)


# Endpoint para obtener especialidades
@router.get("/")
async def get_specialities():
    return [{"id": 1, "name": "Cardiology"}, {"id": 2, "name": "Neurology"}]
