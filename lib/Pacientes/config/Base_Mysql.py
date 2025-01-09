import os
from sqlalchemy import create_engine, MetaData

environment = os.getenv("ENVIRONMENT", "local")

if environment == "docker":
    DATABASE_URL = "mysql+pymysql://pacientes_user:pacientes_pass@mysql_pacientes:3306/Pacientes_DB"
else:
    DATABASE_URL = "mysql+pymysql://pacientes_user:pacientes_pass@127.0.0.1:3600/Pacientes_DB"

engine = create_engine(DATABASE_URL)
conx = engine.connect()
meta_data = MetaData()
