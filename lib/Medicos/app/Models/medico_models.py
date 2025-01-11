from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from lib.Medicos.config.Base_Mysql import engine, meta_data

# Example table definition
medico = Table(
    "Medicos", meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String(15)),
    Column("specialty", String(20)),
    Column("contraseña", String(20))
)

# Create the table in the database
meta_data.create_all(engine)