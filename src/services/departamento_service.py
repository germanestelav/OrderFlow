from sqlalchemy.orm import Session
from models.departamento import Departamento

# Crear un departamento
def create_departamento(db: Session, nombre):
    nuevo_departamento = Departamento(Nombre=nombre)
    db.add(nuevo_departamento)
    db.commit()
    db.refresh(nuevo_departamento)
    return nuevo_departamento

# Obtener todos los departamento
def get_departamentos(db: Session):
    return db.query(Departamento).all()

# Obtener departamento por su ID
def get_departamento_by_id(db: Session, departamento_id):
    return db.query(Departamento).filter(Departamento.DepartamentoID == departamento_id).first()

# Actualizar un departamento
def update_departamento(db: Session, departamento_id, nombre):
    departamento = db.query(Departamento).filter(Departamento.DepartamentoID == departamento_id).first()
    if departamento:
        departamento.Nombre = nombre
        db.commit()
        db.refresh(departamento)
    return departamento

# Eliminar un departamento
def delete_departamento(db: Session, departamento_id):
    departamento = db.query(Departamento).filter(Departamento.DepartamentoID == departamento_id).first()
    if departamento:
        db.delete(departamento)
        db.commit()
    return departamento
