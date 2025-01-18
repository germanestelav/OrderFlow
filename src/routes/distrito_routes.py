from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.distrito_service import (
    get_distritos, get_distrito_by_id, create_distrito, update_distrito, delete_distrito
)

distrito_bp = Blueprint("distritos", __name__)

@distrito_bp.route("/distritos", methods=["GET"])
def get_distritos_endpoint():
    db = next(get_db())
    distritos = get_distritos(db)
    return jsonify([distrito.to_dict() for distrito in distritos])

@distrito_bp.route("/distritos/<int:distrito_id>", methods=["GET"])
def get_distrito_by_id_endpoint(distrito_id):
    db = next(get_db())
    distrito = get_distrito_by_id(db, distrito_id)
    if not distrito:
        return jsonify({"error": "Distrito no encontrado"}), 404
    return jsonify(distrito.to_dict())

@distrito_bp.route("/distritos", methods=["POST"])
def create_distrito_endpoint():
    db = next(get_db())
    data = request.json
    nuevo_distrito = create_distrito(
        db,
        nombre=data.get("Nombre"),
        provincia_id=data.get("ProvinciaID")
    )
    return jsonify(nuevo_distrito.to_dict()), 201

@distrito_bp.route("/distritos/<int:distrito_id>", methods=["PUT"])
def update_distrito_endpoint(distrito_id):
    db = next(get_db())
    data = request.json
    distrito_actualizado = update_distrito(
        db,
        distrito_id=distrito_id,
        nombre=data.get("Nombre"),
        provincia_id=data.get("ProvinciaID")
    )
    if not distrito_actualizado:
        return jsonify({"error": "Distrito no encontrado"}), 404
    return jsonify(distrito_actualizado.to_dict())

@distrito_bp.route("/distritos/<int:distrito_id>", methods=["DELETE"])
def delete_distrito_endpoint(distrito_id):
    db = next(get_db())
    distrito_eliminado = delete_distrito(db, distrito_id)
    if not distrito_eliminado:
        return jsonify({"error": "Distrito no encontrado"}), 404
    return jsonify({"message": "Distrito eliminado con éxito"})
