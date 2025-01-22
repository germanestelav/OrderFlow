from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.promocion_service import (get_promociones, get_promocion_by_id, create_promocion, update_promocion, delete_promocion)

promocion_bp = Blueprint("promociones", __name__)

@promocion_bp.route("/promociones", methods=["GET"])
@jwt_required()
def get_promociones_endpoint():
    db = next(get_db())
    promociones = get_promociones(db)
    return jsonify([promocion.to_dict() for promocion in promociones])

@promocion_bp.route("/promociones/<int:promocion_id>", methods=["GET"])
@jwt_required()
def get_promocion_by_id_endpoint(promocion_id):
    db = next(get_db())
    promocion = get_promocion_by_id(db, promocion_id)
    if not promocion:
        return jsonify({"error": "Promocion no encontrada"}), 404
    return jsonify(promocion.to_dict())

@promocion_bp.route("/promociones", methods=["POST"])
@jwt_required()
def create_promocion_endpoint():
    db: Session = next(get_db())
    data = request.json

    nueva_promocion = create_promocion(
        db,
        nombre=data.get("Nombre"),
        fecha_inicio=data.get("FechaInicio"),
        fecha_fin=data.get("FechaFin"),
        estado=data.get("Estado")
    )
    return jsonify({
        "PromoID": nueva_promocion.PromoID,
        "Nombre": nueva_promocion.Nombre,
        "FechaInicio": str(nueva_promocion.FechaInicio),
        "FechaFin": str(nueva_promocion.FechaFin),
        "Estado": nueva_promocion.Estado.value
    }), 201

@promocion_bp.route("/promociones/<int:promocion_id>", methods=["PUT"])
@jwt_required()
def update_promocion_endpoint(promocion_id):
    db: Session = next(get_db())
    data = request.json

    promocion_actualizada = update_promocion(
        db,
        promocion_id=promocion_id,
        nombre=data.get("Nombre"),
        fecha_inicio=data.get("FechaInicio"),
        fecha_fin=data.get("FechaFin"),
        estado=data.get("Estado")
    )
    if not promocion_actualizada:
        return jsonify({"error": "Promocion no encontrada"}), 404
    return jsonify({
        "PromoID": promocion_actualizada.PromoID,
        "Nombre": promocion_actualizada.Nombre,
        "FechaInicio": str(promocion_actualizada.FechaInicio),
        "FechaFin": str(promocion_actualizada.FechaFin),
        "Estado": promocion_actualizada.Estado.value
    })

@promocion_bp.route("/promociones/<int:promocion_id>", methods=["DELETE"])
@jwt_required()
def delete_promocion_endpoint(promocion_id):
    db: Session = next(get_db())
    promocion_eliminada = delete_promocion(db, promocion_id)
    if not promocion_eliminada:
        return jsonify({"error": "Promocion no encontrada"}), 404
    return jsonify({"message": "Promocion eliminada con exito"})
