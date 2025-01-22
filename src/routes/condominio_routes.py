from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.condominio_service import (
    get_condominios, get_condominio_by_id, create_condominio, update_condominio, delete_condominio
)

condominio_bp = Blueprint("condominios", __name__)

@condominio_bp.route("/condominios", methods=["GET"])
@jwt_required()
def get_condominios_endpoint():
    db: Session = next(get_db())
    condominios = get_condominios(db)
    return jsonify([condominio.to_dict() for condominio in condominios])

@condominio_bp.route("/condominios/<int:condominio_id>", methods=["GET"])
@jwt_required()
def get_condominio_by_id_endpoint(condominio_id):
    db: Session = next(get_db())
    condominio = get_condominio_by_id(db, condominio_id)
    if not condominio:
        return jsonify({"error": "Condominio no encontrado"}), 404
    return jsonify(condominio.to_dict())

@condominio_bp.route("/condominios", methods=["POST"])
@jwt_required()
def create_condominio_endpoint():
    db: Session = next(get_db())
    data = request.json

    nuevo_condominio = create_condominio(
        db,
        nombre=data.get("Nombre"),
        distrito_id=data.get("DistritoID")
    )
    return jsonify(nuevo_condominio.to_dict()), 201

@condominio_bp.route("/condominios/<int:condominio_id>", methods=["PUT"])
@jwt_required()
def update_condominio_endpoint(condominio_id):
    db: Session = next(get_db())
    data = request.json

    condominio_actualizado = update_condominio(
        db,
        condominio_id=condominio_id,
        nombre=data.get("Nombre"),
        distrito_id=data.get("DistritoID")
    )
    if not condominio_actualizado:
        return jsonify({"error": "Condominio no encontrado"}), 404
    return jsonify(condominio_actualizado.to_dict())

@condominio_bp.route("/condominios/<int:condominio_id>", methods=["DELETE"])
@jwt_required()
def delete_condominio_endpoint(condominio_id):
    db: Session = next(get_db())
    condominio_eliminado = delete_condominio(db, condominio_id)
    if not condominio_eliminado:
        return jsonify({"error": "Condominio no encontrado"}), 404
    return jsonify({"message": "Condominio eliminado con éxito"})
