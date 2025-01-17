from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.caja_service import (create_caja, get_cajas, get_caja_by_id, update_caja, delete_caja)

caja_bp = Blueprint("cajas", __name__)

@caja_bp.route("/cajas", methods=["POST"])
def create_caja_endpoint():
    db: Session = next(get_db())
    data = request.json
    codigo = data.get("codigo")
    latitud = data.get("latitud")
    longitud = data.get("longitud")
    if not codigo:
        return jsonify({"error": "El campo 'codigo' es obligatorio"}), 400
    nueva_caja = create_caja(db, codigo, latitud, longitud)
    return jsonify(nueva_caja.to_dict()), 201

@caja_bp.route("/cajas", methods=["GET"])
def get_cajas_endpoint():
    db: Session = next(get_db())
    cajas = get_cajas(db)
    return jsonify([caja.to_dict() for caja in cajas])

@caja_bp.route("/cajas/<int:caja_id>", methods=["GET"])
def get_caja_by_id_endpoint(caja_id):
    db: Session = next(get_db())
    caja = get_caja_by_id(db, caja_id)
    if not caja:
        return jsonify({"error": "Caja no encontrada"}), 404
    return jsonify(caja.to_dict())

@caja_bp.route("/cajas/<int:caja_id>", methods=["PUT"])
def update_caja_endpoint(caja_id):
    db: Session = next(get_db())
    data = request.json
    codigo = data.get("codigo")
    latitud = data.get("latitud")
    longitud = data.get("longitud")
    caja = update_caja(db, caja_id, codigo, latitud, longitud)
    if not caja:
        return jsonify({"error": "Caja no encontrada"}), 404
    return jsonify(caja.to_dict())

@caja_bp.route("/cajas/<int:caja_id>", methods=["DELETE"])
def delete_caja_endpoint(caja_id):
    db: Session = next(get_db())
    caja = delete_caja(db, caja_id)
    if not caja:
        return jsonify({"error": "Caja no encontrada"}), 404
    return jsonify({"message": "Caja eliminada con éxito"})
