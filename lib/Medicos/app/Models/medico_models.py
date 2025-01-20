from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from lib.Medicos.config.Base_Mysql import engine, meta_data

# Example table definition
medico_table = Table(
    "Medicos",
    meta_data,
    Column("Cedula", Integer, primary_key=True),
    Column("Primer_Nombre", String(15), nullable=False),
    Column("Segundo_Nombre", String(15)),
    Column("Primer_Apellido", String(15), nullable=False),
    Column("Segundo_Apellido", String(15)),
    Column("Especialidad", String(20)),
    Column("Contraseña", String(10), nullable=False),
)

# Create the table in the database
meta_data.create_all(engine)
