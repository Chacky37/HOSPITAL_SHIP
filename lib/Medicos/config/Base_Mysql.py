import os
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://medicos_user:medicos_pass@mysql_medicos:3306/Medicos_DB")
engine = create_engine(DATABASE_URL)
conx = engine.connect()
meta_data = MetaData()
