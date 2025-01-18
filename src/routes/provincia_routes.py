from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.provincia_service import (
    get_provincias, get_provincia_by_id, create_provincia, update_provincia, delete_provincia
)

provincia_bp = Blueprint("provincias", __name__)

@provincia_bp.route("/provincias", methods=["GET"])
def get_provincias_endpoint():
    db = next(get_db())
    provincias = get_provincias(db)
    return jsonify([provincia.to_dict() for provincia in provincias])

@provincia_bp.route("/provincias/<int:provincia_id>", methods=["GET"])
def get_provincia_by_id_endpoint(provincia_id):
    db = next(get_db())
    provincia = get_provincia_by_id(db, provincia_id)
    if not provincia:
        return jsonify({"error": "Provincia no encontrada"}), 404
    return jsonify(provincia.to_dict())

@provincia_bp.route("/provincias", methods=["POST"])
def create_provincia_endpoint():
    db = next(get_db())
    data = request.json
    nueva_provincia = create_provincia(
        db,
        nombre=data.get("Nombre"),
        departamento_id=data.get("DepartamentoID")
    )
    return jsonify(nueva_provincia.to_dict()), 201

@provincia_bp.route("/provincias/<int:provincia_id>", methods=["PUT"])
def update_provincia_endpoint(provincia_id):
    db = next(get_db())
    data = request.json
    provincia_actualizada = update_provincia(
        db,
        provincia_id=provincia_id,
        nombre=data.get("Nombre"),
        departamento_id=data.get("DepartamentoID")
    )
    if not provincia_actualizada:
        return jsonify({"error": "Provincia no encontrada"}), 404
    return jsonify(provincia_actualizada.to_dict())

@provincia_bp.route("/provincias/<int:provincia_id>", methods=["DELETE"])
def delete_provincia_endpoint(provincia_id):
    db = next(get_db())
    provincia_eliminada = delete_provincia(db, provincia_id)
    if not provincia_eliminada:
        return jsonify({"error": "Provincia no encontrada"}), 404
    return jsonify({"message": "Provincia eliminada con éxito"})
