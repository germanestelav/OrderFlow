from flask import Blueprint, request, jsonify
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from services.rol_service import (
    get_roles, get_rol_by_id, create_rol, update_rol, delete_rol
)

rol_bp = Blueprint("roles", __name__)

@rol_bp.route("/roles", methods=["GET"])
def get_roles_endpoint():
    db = next(get_db())
    roles = get_roles(db)
    return jsonify([rol.to_dict() for rol in roles])

@rol_bp.route("/roles/<int:rol_id>", methods=["GET"])
def get_rol_by_id_endpoint(rol_id):
    db = next(get_db())
    rol = get_rol_by_id(db, rol_id)
    if not rol:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol.to_dict())

@rol_bp.route("/roles", methods=["POST"])
def create_rol_endpoint():
    db: Session = next(get_db())
    data = request.json
    nuevo_rol = create_rol(db, nombre_rol=data.get("NombreRol"))
    return jsonify({"RolID": nuevo_rol.RolID, "NombreRol": nuevo_rol.NombreRol}), 201

@rol_bp.route("/roles/<int:rol_id>", methods=["PUT"])
def update_rol_endpoint(rol_id):
    db: Session = next(get_db())
    data = request.json
    rol_actualizado = update_rol(db, rol_id, nombre_rol=data.get("NombreRol"))
    if not rol_actualizado:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify({"RolID": rol_actualizado.RolID, "NombreRol": rol_actualizado.NombreRol})

@rol_bp.route("/roles/<int:rol_id>", methods=["DELETE"])
def delete_rol_endpoint(rol_id):
    db: Session = next(get_db())
    rol_eliminado = delete_rol(db, rol_id)
    if not rol_eliminado:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify({"message": "Rol eliminado con éxito"})
