import os
from sqlalchemy import create_engine, MetaData

environment = os.getenv("ENVIRONMENT", "local")

if environment == "docker":
    DATABASE_URL = "mysql+pymysql://medicos_user:medicos_pass@mysql_medicos:3306/Medicos_DB"
else:
    DATABASE_URL = "mysql+pymysql://medicos_user:medicos_pass@localhost:3500/Medicos_DB"

engine = create_engine(DATABASE_URL)

conx = engine.connect()
meta_data = MetaData()
