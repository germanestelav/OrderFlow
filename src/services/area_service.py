from sqlalchemy.orm import Session
from models.area import Area

# Crear un área
def create_area(db: Session, nombre: str) -> Area:
    nueva_area = Area(Nombre=nombre)
    db.add(nueva_area)
    db.commit()
    db.refresh(nueva_area)
    return nueva_area

# Obtener todas las áreas
def get_areas(db: Session):
    return db.query(Area).all()

# Obtener un área por su ID
def get_area_by_id(db: Session, area_id: int):
    return db.query(Area).filter(Area.AreaID == area_id).first()

# Actualizar un área
def update_area(db: Session, area_id: int, nombre: str):
    area = db.query(Area).filter(Area.AreaID == area_id).first()
    if area:
        area.Nombre = nombre
        db.commit()
        db.refresh(area)
    return area

# Eliminar un área
def delete_area(db: Session, area_id: int):
    area = db.query(Area).filter(Area.AreaID == area_id).first()
    if area:
        db.delete(area)
        db.commit()
    return area
