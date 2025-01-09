from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from lib.Pacientes.config.Base_Mysql import engine, meta_data

# Example table definition
enlace_paciente = Table(
    "pacientes", meta_data,
    Column("cedula", Integer, primary_key=True),
    Column("nombre", String(15)),
    Column("edad", Integer)
)

# Create the table in the database
meta_data.create_all(engine)