from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from lib.Pacientes.config.Base_Mysql import engine, meta_data

paciente_table = Table(
    "Pacientes",
    meta_data,
    Column("Cedula", Integer, primary_key=True),
    Column("Nombre", String(15)),
    Column("Edad", Integer),
)

meta_data.create_all(engine)
