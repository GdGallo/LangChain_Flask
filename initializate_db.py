from database.db_config import Base, engine
from database.models import News, Project, Memory

# Crear las tablas en la base de datos
if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)
    print("Base de datos inizializada.")