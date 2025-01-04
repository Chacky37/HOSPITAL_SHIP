from fastapi import FastAPI
from lib.Medicos.run import app as medico_app
from lib.Pacientes.run import app as paciente_app

# Instancia principal de FastAPI
app = FastAPI(
    title="Hospital API",
    description="API principal que monta subrutas para médicos y pacientes",
    version="1.0.0",
)

# Montar las sub-APIs
app.mount("/medicos", medico_app)
#app.mount("/pacientes", paciente_app)
