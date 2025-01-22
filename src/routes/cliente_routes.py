from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from database.db_mysql import get_db
from sqlalchemy.orm import Session
from models.cliente import Cliente
from datetime import date, datetime
from services.cliente_service import (
    get_clientes,
    get_cliente_by_id,
    create_cliente,
    update_cliente,
    delete_cliente, get_cliente_by_name_or_id
)

cliente_bp = Blueprint("clientes", __name__)

@cliente_bp.route("/clientes", methods=["GET"])
@jwt_required()
def get_clientes_endpoint():
    db: Session = next(get_db())

    # Parámetros de paginación
    page = int(request.args.get("page", 1))  # Página actual (por defecto 1)
    per_page = int(request.args.get("per_page", 50))  # Clientes por página (por defecto 50)

    # Parámetros de rango de fechas
    fecha_inicio = request.args.get("fecha_inicio")  # Formato esperado: YYYY-MM-DD
    fecha_fin = request.args.get("fecha_fin")  # Formato esperado: YYYY-MM-DD

    # Si no se proporcionan fechas, usar por defecto el día actual
    if not fecha_inicio and not fecha_fin:
        hoy = date.today()
        fecha_inicio = hoy
        fecha_fin = hoy

    # Convertir fechas a formato datetime
    try:
        fecha_inicio = datetime.strptime(str(fecha_inicio), "%Y-%m-%d").date()
        fecha_fin = datetime.strptime(str(fecha_fin), "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD."}), 400

    # Consulta para obtener los clientes en el rango de fechas
    clientes_query = db.query(Cliente).filter(
        Cliente.Fecha >= fecha_inicio,
        Cliente.Fecha <= fecha_fin
    )

    # Total de clientes
    total = clientes_query.count()

    # Aplicar paginación
    clientes = clientes_query.offset((page - 1) * per_page).limit(per_page).all()

    if not clientes:
        return jsonify({"message": "No se encontraron clientes en el rango especificado"}), 404

    # Retornar los resultados con información de paginación
    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "fecha_inicio": str(fecha_inicio),
        "fecha_fin": str(fecha_fin),
        "results": [cliente.to_dict() for cliente in clientes]
    }), 200

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["GET"])
@jwt_required()
def get_cliente_by_id_endpoint(cliente_id):
    db = next(get_db())
    cliente = get_cliente_by_id(db, cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(cliente.to_dict())

@cliente_bp.route("/clientes/buscar", methods=["GET"])
@jwt_required()
def search_cliente_endpoint():
    db: Session = next(get_db())

    # Obtener parámetros de búsqueda y paginación
    query = request.args.get("query", "").strip()
    page = int(request.args.get("page", 1))  # Página actual
    per_page = int(request.args.get("per_page", 50))  # Clientes por página

    if not query:
        return jsonify({"error": "Debe proporcionar un término de búsqueda"}), 400

    # Realizar la consulta con paginación
    clientes_query = db.query(Cliente).filter(
        (Cliente.NombreCompleto.like(f"%{query}%")) | (Cliente.NumeroIdentificacion == query)
    )

    # Total de resultados
    total = clientes_query.count()

    # Aplicar paginación
    clientes = clientes_query.offset((page - 1) * per_page).limit(per_page).all()

    if not clientes:
        return jsonify({"message": "No se encontraron clientes que coincidan con el criterio"}), 404

    # Retornar los resultados con información de paginación
    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "results": [cliente.to_dict() for cliente in clientes]
    }), 200


@cliente_bp.route("/clientes", methods=["POST"])
@jwt_required()  # Asegura que el token JWT esté presente y sea válido
def create_cliente_endpoint():
    db: Session = next(get_db())
    data = request.json

    try:
        # Extraer el UsuarioID del token de autenticación
        usuario_id = int(get_jwt_identity())  # Ahora extraemos directamente el ID
        print(f"UsuarioID extraído: {usuario_id}")  # Depuración

        # Llamamos a la función del servicio con los datos del cliente y UsuarioID
        nuevo_cliente = create_cliente(db, data, usuario_id)
        print(f"Cliente creado exitosamente: {nuevo_cliente.to_dict()}")  # Depuración

        return jsonify(nuevo_cliente.to_dict()), 201
    except ValueError as e:
        print(f"Error de validación: {str(e)}")  # Depuración
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Error inesperado: {str(e)}")  # Depuración
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500
    
@cliente_bp.route("/clientes/<int:cliente_id>", methods=["PUT"])
@jwt_required()
def update_cliente_endpoint(cliente_id):
    db: Session = next(get_db())
    data = request.json

    try:
        cliente_actualizado = update_cliente(db, cliente_id, data)
        if not cliente_actualizado:
            return jsonify({"error": "Cliente no encontrado"}), 404
        return jsonify(cliente_actualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado.", "details": str(e)}), 500

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["DELETE"])
@jwt_required()
def delete_cliente_endpoint(cliente_id):
    db: Session = next(get_db())
    cliente_eliminado = delete_cliente(db, cliente_id)
    if not cliente_eliminado:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify({"message": "Cliente eliminado con éxito"})
