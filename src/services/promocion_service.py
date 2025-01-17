from models.promocion import Promocion

# Crear una nueva promocion
def create_promocion(db, nombre, fecha_inicio, fecha_fin, estado):
    nueva_promocion = Promocion(
        Nombre=nombre,
        FechaInicio=fecha_inicio,
        FechaFin=fecha_fin,
        Estado=estado
    )
    db.add(nueva_promocion)
    db.commit()
    db.refresh(nueva_promocion)
    return nueva_promocion

# Obtener todos las promociones
def get_promociones(db):
    return db.query(Promocion).all()

# Obtener promociones por ID
def get_promocion_by_id(db, promocion_id):
    return db.query(Promocion).filter(Promocion.PromoID == promocion_id).first()

# Actualizar una promocion
def update_promocion(db, promocion_id, nombre, fecha_inicio, fecha_fin, estado):
    promocion = get_promocion_by_id(db, promocion_id)
    if not promocion:
        return None

    promocion.Nombre = nombre
    promocion.FechaInicio = fecha_inicio
    promocion.FechaFin = fecha_fin
    promocion.Estado = estado

    db.commit()
    db.refresh(promocion)
    return promocion

# Eliminar una promocion
def delete_promocion(db, promocion_id):
    promocion = get_promocion_by_id(db, promocion_id)
    if not promocion:
        return None

    db.delete(promocion)
    db.commit()
    return promocion
