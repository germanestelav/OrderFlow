import sys
import os

# Agrega el directorio 'src' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from flask_jwt_extended import JWTManager, create_access_token
from services.auth_service import verificar_credenciales
from database.db_mysql import get_db
from flask_cors import CORS
from flask import Flask, jsonify, request
from routes.area_routes import area_bp
from routes.caja_routes import caja_bp
from routes.departamento_routes import departamento_bp
from routes.estado_cliente_routes import estado_cliente_bp
from routes.plan_routes import plan_bp
from routes.promocion_routes import promocion_bp
from routes.rol_routes import rol_bp
from routes.tipo_servicio_routes import tipo_servicio_bp
from routes.provincia_routes import provincia_bp
from routes.distrito_routes import distrito_bp
from routes.condominio_routes import condominio_bp
from routes.usuario_routes import usuario_bp
from routes.usuario_rol_routes import usuario_rol_bp
from routes.cliente_routes import cliente_bp
from routes.cliente_usuario_routes import cliente_usuario_bp
from routes.comentariosclientes_routes import comentarios_clientes_bp

app = Flask(__name__)

# Configurar CORS para permitir solicitudes desde cualquier origen
CORS(app)

# # Configurar CORS para permitir solo solicitudes desde un dominio específico
# CORS(app, resources={r"/api/*": {"origins": "http://tudominio.com"}})

# Configurar clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "clave_secreta_super_segura"  # Cambia esto por una clave segura
jwt = JWTManager(app)  # Inicialización correcta

# Ruta de autenticación
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    # Verificar credenciales usando tu servicio
    db = next(get_db())
    usuario = verificar_credenciales(db, username, password)

    if usuario:
        access_token = create_access_token(identity=str(usuario.UsuarioID))  # Ahora es solo el ID del usuario
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Registrar las rutas de áreas
app.register_blueprint(area_bp, url_prefix="/api")
app.register_blueprint(caja_bp, url_prefix="/api")
app.register_blueprint(departamento_bp, url_prefix="/api")
app.register_blueprint(estado_cliente_bp, url_prefix="/api")
app.register_blueprint(plan_bp, url_prefix="/api")
app.register_blueprint(promocion_bp, url_prefix="/api")
app.register_blueprint(rol_bp, url_prefix="/api")
app.register_blueprint(tipo_servicio_bp, url_prefix="/api")
app.register_blueprint(provincia_bp, url_prefix="/api")
app.register_blueprint(distrito_bp, url_prefix="/api")
app.register_blueprint(condominio_bp, url_prefix="/api")
app.register_blueprint(usuario_bp, url_prefix="/api")
app.register_blueprint(usuario_rol_bp, url_prefix="/api")
app.register_blueprint(cliente_bp, url_prefix="/api")
app.register_blueprint(cliente_usuario_bp, url_prefix="/api")
app.register_blueprint(comentarios_clientes_bp, url_prefix="/api")

@app.route("/")
def root():
    return {"message": "API de Áreas Activa"}


if __name__ == "__main__":
    app.run(debug=True)
