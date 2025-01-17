from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.estado_cliente_service import (create_estado_cliente, get_estados_cliente, get_estado_cliente_by_id, update_estado_cliente, delete_estado_cliente,)

estado_cliente_bp = Blueprint("estados_cliente", __name__)

@estado_cliente_bp.route("/estadoscliente", methods=["POST"])
def create_estado_cliente_endpoint():
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    nuevo_estado = create_estado_cliente(db, nombre)
    return jsonify(nuevo_estado.to_dict()), 201

@estado_cliente_bp.route("/estadoscliente", methods=["GET"])
def get_estados_cliente_endpoint():
    db: Session = next(get_db())
    estados = get_estados_cliente(db)
    return jsonify([estado.to_dict() for estado in estados])

@estado_cliente_bp.route("/estadoscliente/<int:estado_id>", methods=["GET"])
def get_estado_cliente_by_id_endpoint(estado_id):
    db: Session = next(get_db())
    estado = get_estado_cliente_by_id(db, estado_id)
    if not estado:
        return jsonify({"error": "Estado no encontrado"}), 404
    return jsonify(estado.to_dict())

@estado_cliente_bp.route("/estadoscliente/<int:estado_id>", methods=["PUT"])
def update_estado_cliente_endpoint(estado_id):
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    estado = update_estado_cliente(db, estado_id, nombre)
    if not estado:
        return jsonify({"error": "Estado no encontrado"}), 404
    return jsonify(estado.to_dict())

@estado_cliente_bp.route("/estadoscliente/<int:estado_id>", methods=["DELETE"])
def delete_estado_cliente_endpoint(estado_id):
    db: Session = next(get_db())
    estado = delete_estado_cliente(db, estado_id)
    if not estado:
        return jsonify({"error": "Estado no encontrado"}), 404
    return jsonify({"message": "Estado eliminado con éxito"})
