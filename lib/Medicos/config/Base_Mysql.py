from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Configurar el motor de base de datos
DATABASE_URL = "mysql+pymysql://root:saul123@localhost:3306/Users_Medicos"
engine = create_engine(DATABASE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear metadatos
meta_data = MetaData()

# Dependencia para obtener la sesión en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db  # ✅ Cede la sesión para ser usada
    finally:
        db.close()  # ✅ Cierra la sesión después de cada solicitud
