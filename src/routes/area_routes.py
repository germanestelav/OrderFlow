from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from database.db_mysql import get_db
from services.area_service import (create_area, get_areas, get_area_by_id, update_area, delete_area)

# Crear un Blueprint para las rutas de áreas
area_bp = Blueprint("areas", __name__)

@area_bp.route("/areas", methods=["POST"])
def create_area_endpoint():
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    nueva_area = create_area(db, nombre)
    return jsonify({"AreaID": nueva_area.AreaID, "Nombre": nueva_area.Nombre}), 201

@area_bp.route("/areas", methods=["GET"])
def get_areas_endpoint():
    db: Session = next(get_db())
    areas = get_areas(db)
    return jsonify([{"AreaID": area.AreaID, "Nombre": area.Nombre} for area in areas])

@area_bp.route("/areas/<int:area_id>", methods=["GET"])
def get_area_by_id_endpoint(area_id):
    db: Session = next(get_db())
    area = get_area_by_id(db, area_id)
    if not area:
        return jsonify({"error": "Área no encontrada"}), 404
    return jsonify({"AreaID": area.AreaID, "Nombre": area.Nombre})

@area_bp.route("/areas/<int:area_id>", methods=["PUT"])
def update_area_endpoint(area_id):
    db: Session = next(get_db())
    data = request.json
    nombre = data.get("nombre")
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    area = update_area(db, area_id, nombre)
    if not area:
        return jsonify({"error": "Área no encontrada"}), 404
    return jsonify({"AreaID": area.AreaID, "Nombre": area.Nombre})

@area_bp.route("/areas/<int:area_id>", methods=["DELETE"])
def delete_area_endpoint(area_id):
    db: Session = next(get_db())
    area = delete_area(db, area_id)
    if not area:
        return jsonify({"error": "Área no encontrada"}), 404
    return jsonify({"message": "Área eliminada con éxito"})
