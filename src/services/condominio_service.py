from sqlalchemy.orm import Session
from models.condominio import Condominio

# Obtener todos los condominios
def get_condominios(db):
    return db.query(Condominio).all()

# Obtener un condominio por ID
def get_condominio_by_id(db, condominio_id):
    return db.query(Condominio).filter(Condominio.CondominioID == condominio_id).first()

# Crear una condominio
def create_condominio(db, nombre, distrito_id):
    nuevo_condominio = Condominio(
        Nombre=nombre,
        DistritoID=distrito_id
    )
    db.add(nuevo_condominio)
    db.commit()
    db.refresh(nuevo_condominio)
    return nuevo_condominio

# Editar un condominio
def update_condominio(db, condominio_id, nombre, distrito_id):
    condominio = get_condominio_by_id(db, condominio_id)
    if not condominio:
        return None

    condominio.Nombre = nombre
    condominio.DistritoID = distrito_id

    db.commit()
    db.refresh(condominio)
    return condominio

# Eliminar un condominio
def delete_condominio(db, condominio_id):
    condominio = get_condominio_by_id(db, condominio_id)
    if not condominio:
        return None

    db.delete(condominio)
    db.commit()
    return condominio
