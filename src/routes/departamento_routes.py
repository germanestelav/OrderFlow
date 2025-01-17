from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.departamento_service import (create_departamento, get_departamentos, get_departamento_by_id, update_departamento, delete_departamento)

# Crear un Blueprint para las rutas departamentos
departamento_bp = Blueprint("departamentos", __name__)

@departamento_bp.route("/departamentos", methods=["POST"])
def create_departamento_endpoint():
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    nuevo_departamento = create_departamento(db, nombre)
    return jsonify(nuevo_departamento.to_dict()), 201

@departamento_bp.route("/departamentos", methods=["GET"])
def get_departamentos_endpoint():
    db: Session = next(get_db())
    departamentos = get_departamentos(db)
    return jsonify([departamento.to_dict() for departamento in departamentos])

@departamento_bp.route("/departamentos/<int:departamento_id>", methods=["GET"])
def get_departamento_by_id_endpoint(departamento_id):
    db: Session = next(get_db())
    departamento = get_departamento_by_id(db, departamento_id)
    if not departamento:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return jsonify(departamento.to_dict())

@departamento_bp.route("/departamentos/<int:departamento_id>", methods=["PUT"])
def update_departamento_endpoint(departamento_id):
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    departamento = update_departamento(db, departamento_id, nombre)
    if not departamento:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return jsonify(departamento.to_dict())

@departamento_bp.route("/departamentos/<int:departamento_id>", methods=["DELETE"])
def delete_departamento_endpoint(departamento_id):
    db: Session = next(get_db())
    departamento = delete_departamento(db, departamento_id)
    if not departamento:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return jsonify({"message": "Departamento eliminado con éxito"})
