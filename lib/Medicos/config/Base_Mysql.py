import os
from sqlalchemy import create_engine, MetaData


if os.getenv("ENVIRONMENT") == "docker":
    DATABASE_URL = "mysql+pymysql://medicos_user:medicos_pass@mysql_medicos:3306/Medicos_DB"
else:
    DATABASE_URL = "mysql+pymysql://medicos_user:medicos_pass@localhost:3500/Medicos_DB"
   
   
engine = create_engine(DATABASE_URL)

meta_data = MetaData()
