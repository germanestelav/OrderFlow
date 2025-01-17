from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from models.plan import EstadoEnum
from services.plan_service import (create_plan, get_planes, get_plan_by_id, update_plan, delete_plan)

plan_bp = Blueprint("planes", __name__)

@plan_bp.route("/planes", methods=["POST"])
def create_plan_endpoint():
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    fecha_inicio = data.get("fecha_inicio")
    fecha_fin = data.get("fecha_fin")
    estado = data.get("estado", "Inactivo")

    # Validar valores
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    if estado not in [e.value for e in EstadoEnum]:
        return jsonify({"error": f"El campo 'estado' debe ser uno de {[e.value for e in EstadoEnum]}"}), 400

    nuevo_plan = create_plan(db, nombre, fecha_inicio, fecha_fin, EstadoEnum(estado))
    return jsonify(nuevo_plan.to_dict()), 201

@plan_bp.route("/planes", methods=["GET"])
def get_planes_endpoint():
    db: Session = next(get_db())
    planes = get_planes(db)
    return jsonify([plan.to_dict() for plan in planes])

@plan_bp.route("/planes/<int:plan_id>", methods=["GET"])
def get_plan_by_id_endpoint(plan_id):
    db: Session = next(get_db())
    plan = get_plan_by_id(db, plan_id)
    if not plan:
        return jsonify({"error": "Plan no encontrado"}), 404
    return jsonify(plan.to_dict())

@plan_bp.route("/planes/<int:plan_id>", methods=["PUT"])
def update_plan_endpoint(plan_id):
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    fecha_inicio = data.get("fecha_inicio")
    fecha_fin = data.get("fecha_fin")
    estado = data.get("estado")

    # Validar valores
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    if estado not in [e.value for e in EstadoEnum]:
        return jsonify({"error": f"El campo 'estado' debe ser uno de {[e.value for e in EstadoEnum]}"}), 400

    plan = update_plan(db, plan_id, nombre, fecha_inicio, fecha_fin, EstadoEnum(estado))
    if not plan:
        return jsonify({"error": "Plan no encontrado"}), 404
    return jsonify(plan.to_dict())

@plan_bp.route("/planes/<int:plan_id>", methods=["DELETE"])
def delete_plan_endpoint(plan_id):
    db: Session = next(get_db())
    plan = delete_plan(db, plan_id)
    if not plan:
        return jsonify({"error": "Plan no encontrado"}), 404
    return jsonify({"message": "Plan eliminado con éxito"})
