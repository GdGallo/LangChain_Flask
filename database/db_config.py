from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Crear la base de datos SQLite
DATABASE_URL = "sqlite:///oficina_virtual.db"

# Inicializar la base declarativa
Base = declarative_base()

# Configurar el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configurar la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
