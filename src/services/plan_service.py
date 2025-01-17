from sqlalchemy.orm import Session
from models.plan import Plan

# Crear una nuevo plan
def create_plan(db: Session, nombre, fecha_inicio, fecha_fin, estado):
    nuevo_plan = Plan(
        Nombre=nombre,
        FechaInicio=fecha_inicio,
        FechaFin=fecha_fin,
        Estado=estado,
    )
    db.add(nuevo_plan)
    db.commit()
    db.refresh(nuevo_plan)
    return nuevo_plan

# Obtener todos los planes
def get_planes(db: Session):
    return db.query(Plan).all()

# Obtener los planes por ID
def get_plan_by_id(db: Session, plan_id):
    return db.query(Plan).filter(Plan.PlanID == plan_id).first()

# Actualizar un plan
def update_plan(db: Session, plan_id, nombre, fecha_inicio, fecha_fin, estado):
    plan = db.query(Plan).filter(Plan.PlanID == plan_id).first()
    if plan:
        plan.Nombre = nombre
        plan.FechaInicio = fecha_inicio
        plan.FechaFin = fecha_fin
        plan.Estado = estado
        db.commit()
        db.refresh(plan)
    return plan

# Eliminar un plan
def delete_plan(db: Session, plan_id):
    plan = db.query(Plan).filter(Plan.PlanID == plan_id).first()
    if plan:
        db.delete(plan)
        db.commit()
    return plan
