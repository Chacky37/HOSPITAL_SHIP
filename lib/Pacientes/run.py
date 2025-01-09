from fastapi import FastAPI
from lib.Pacientes.app.Routers import  paciente_router

app = FastAPI(
    title="Pacientes API",
    description="API para gestionar pacientes y especialidades",
    version="1.0.0",
)

# Incluimos los routers
app.include_router(paciente_router.router)
#app.include_router(speciality_router.router)
