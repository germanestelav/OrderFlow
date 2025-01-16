import sys
import os

# Agrega el directorio 'src' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from database.db_mysql import SessionLocal
from models.area import Area

def consultar_areas():
    # Crear una sesión
    db = SessionLocal()

    try:
        # Consultar todas las áreas
        areas = db.query(Area).all()
        print("Áreas registradas en la base de datos:")
        for area in areas:
            print(f"Área ID: {area.AreaID}, Nombre: {area.Nombre}")
    except Exception as e:
        print(f"Error al consultar las áreas: {e}")
    finally:
        # Cerrar la sesión
        db.close()

if __name__ == "__main__":
    consultar_areas()
