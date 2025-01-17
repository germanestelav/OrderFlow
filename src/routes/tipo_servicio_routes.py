from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.tipo_servicio_service import (
    get_tipos_servicio, get_tipo_servicio_by_id, create_tipo_servicio, update_tipo_servicio, delete_tipo_servicio
)

tipo_servicio_bp = Blueprint("tipos_servicio", __name__)

@tipo_servicio_bp.route("/tipos-servicio", methods=["GET"])
def get_tipos_servicio_endpoint():
    db = next(get_db())
    tipos_servicio = get_tipos_servicio(db)
    return jsonify([tipo_servicio.to_dict() for tipo_servicio in tipos_servicio])

@tipo_servicio_bp.route("/tipos-servicio/<int:tipo_servicio_id>", methods=["GET"])
def get_tipo_servicio_by_id_endpoint(tipo_servicio_id):
    db = next(get_db())
    tipo_servicio = get_tipo_servicio_by_id(db, tipo_servicio_id)
    if not tipo_servicio:
        return jsonify({"error": "Tipo de servicio no encontrado"}), 404
    return jsonify(tipo_servicio.to_dict())

@tipo_servicio_bp.route("/tipos-servicio", methods=["POST"])
def create_tipo_servicio_endpoint():
    db = next(get_db())
    data = request.json
    nuevo_tipo_servicio = create_tipo_servicio(db, nombre=data.get("Nombre"))
    return jsonify(nuevo_tipo_servicio.to_dict()), 201

@tipo_servicio_bp.route("/tipos-servicio/<int:tipo_servicio_id>", methods=["PUT"])
def update_tipo_servicio_endpoint(tipo_servicio_id):
    db = next(get_db())
    data = request.json
    tipo_servicio_actualizado = update_tipo_servicio(db, tipo_servicio_id, nombre=data.get("Nombre"))
    if not tipo_servicio_actualizado:
        return jsonify({"error": "Tipo de servicio no encontrado"}), 404
    return jsonify(tipo_servicio_actualizado.to_dict())

@tipo_servicio_bp.route("/tipos-servicio/<int:tipo_servicio_id>", methods=["DELETE"])
def delete_tipo_servicio_endpoint(tipo_servicio_id):
    db = next(get_db())
    tipo_servicio_eliminado = delete_tipo_servicio(db, tipo_servicio_id)
    if not tipo_servicio_eliminado:
        return jsonify({"error": "Tipo de servicio no encontrado"}), 404
    return jsonify({"message": "Tipo de servicio eliminado con éxito"})
