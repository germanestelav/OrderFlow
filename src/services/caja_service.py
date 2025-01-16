from sqlalchemy.orm import Session
from models.caja import Caja

# Crear una caja
def create_caja(db: Session, codigo, latitud, longitud):
    nueva_caja = Caja(codigo=codigo, latitud=latitud, longitud=longitud)
    db.add(nueva_caja)
    db.commit()
    db.refresh(nueva_caja)
    return nueva_caja

# Obtener todas las
def get_cajas(db):
    return db.query(Caja).all()

def get_caja_by_id(db, caja_id):
    return db.query(Caja).filter(Caja.cajaID == caja_id).first()

# Actualizar una caja
def update_caja(db: Session, caja_id, codigo, latitud, longitud):
    caja = db.query(Caja).filter(Caja.cajaID == caja_id).first()
    if caja:
        caja.codigo = codigo
        caja.latitud = latitud
        caja.longitud = longitud
        db.commit()
        db.refresh(caja)
    return caja

# Eliminar una caja
def delete_caja(db: Session, caja_id):
    caja = db.query(Caja).filter(Caja.cajaID == caja_id).first()
    if caja:
        db.delete(caja)
        db.commit()
    return caja
