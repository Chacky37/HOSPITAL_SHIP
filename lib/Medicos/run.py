from fastapi import FastAPI
from lib.Medicos.app.Routers import medico_router, speciality_router

app = FastAPI(
    title="Medicos API",
    description="API para gestionar médicos y especialidades",
    version="1.0.0",
)

# Incluimos los routers
app.include_router(medico_router.router)
# app.include_router(speciality_router.router)
