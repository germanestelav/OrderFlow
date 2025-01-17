from models.tipo_servicio import TipoServicio

# Crear un tipo de servicio
def create_tipo_servicio(db, nombre):
    nuevo_tipo_servicio = TipoServicio(Nombre=nombre)
    db.add(nuevo_tipo_servicio)
    db.commit()
    db.refresh(nuevo_tipo_servicio)
    return nuevo_tipo_servicio

# Obtener todos los servicios
def get_tipos_servicio(db):
    return db.query(TipoServicio).all()

# Obtener los servicios por ID
def get_tipo_servicio_by_id(db, tipo_servicio_id):
    return db.query(TipoServicio).filter(TipoServicio.TipoServicioID == tipo_servicio_id).first()

# Actualizar un servicio
def update_tipo_servicio(db, tipo_servicio_id, nombre):
    tipo_servicio = get_tipo_servicio_by_id(db, tipo_servicio_id)
    if not tipo_servicio:
        return None

    tipo_servicio.Nombre = nombre
    db.commit()
    db.refresh(tipo_servicio)
    return tipo_servicio

# Eliminar un servicio
def delete_tipo_servicio(db, tipo_servicio_id):
    tipo_servicio = get_tipo_servicio_by_id(db, tipo_servicio_id)
    if not tipo_servicio:
        return None

    db.delete(tipo_servicio)
    db.commit()
    return tipo_servicio
