import sys
import os

# Agrega el directorio 'src' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlalchemy import inspect
from database.db_mysql import engine

def inspect_database():
    # Crear el inspector
    inspector = inspect(engine)

    # Listar todas las tablas existentes
    print("Tablas existentes:")
    for table_name in inspector.get_table_names():
        print(f"- {table_name}")

    # Inspeccionar las columnas de una tabla específica
    table_name = "areas"  # Cambia esto por la tabla que quieras inspeccionar
    print(f"\nColumnas de la tabla '{table_name}':")
    columns = inspector.get_columns(table_name)
    for column in columns:
        print(f"- {column['name']} ({column['type']})")

if __name__ == "__main__":
    inspect_database()
