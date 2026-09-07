# routes/auth.py
from flask import Blueprint, jsonify, request
from services.user_service import UserService
from services.jwt_service import JWTService
from models.user import User
from extensions import db

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.post("/register")
def register():
    """Registrar un nuevo usuario"""
    data = request.get_json() or {}
    
    # Validar datos requeridos
    if not data.get('email') or not data.get('password') or not data.get('name'):
        return jsonify({"error": "Email, password y name son requeridos"}), 400
    
    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "El usuario con este email ya existe"}), 409
    
    try:
        # Crear nuevo usuario
        user = User(
            name=data['name'],
            email=data['email']
        )
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            "message": "Usuario registrado exitosamente",
            "user": user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear usuario"}), 500

@auth_bp.post("/login")
def login():
    """Iniciar sesión de usuario"""
    data = request.get_json() or {}
    
    # Validar datos requeridos
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email y password son requeridos"}), 400
    
    # Buscar usuario por email
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    if not user.is_active:
        return jsonify({"error": "Usuario desactivado"}), 401
    
    # Actualizar último login
    user.update_last_login()
    
    # Generar tokens JWT
    access_token = JWTService.generate_token(user.id, user.email)
    refresh_token = JWTService.generate_refresh_token(user.id)
    
    return jsonify({
        "message": "Login exitoso",
        "user": user.to_dict(),
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }), 200

@auth_bp.post("/logout")
def logout():
    """Cerrar sesión de usuario"""
    auth_header = request.headers.get('Authorization')
    token = JWTService.extract_token_from_header(auth_header)
    
    if not token:
        return jsonify({"error": "Token de autorización requerido"}), 401
    
    # Validar el token
    payload = JWTService.decode_token(token)
    if not payload:
        return jsonify({"error": "Token inválido o expirado"}), 401
    
    # Agregar token a la lista negra
    JWTService.blacklist_token(token)
    
    return jsonify({"message": "Logout exitoso"}), 200

@auth_bp.get("/me")
def get_current_user():
    """Obtener información del usuario actual"""
    auth_header = request.headers.get('Authorization')
    token = JWTService.extract_token_from_header(auth_header)
    
    if not token:
        return jsonify({"error": "Token de autorización requerido"}), 401
    
    # Validar el token
    payload = JWTService.decode_token(token)
    if not payload:
        return jsonify({"error": "Token inválido o expirado"}), 401
    
    user = User.query.get(payload['user_id'])
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    return jsonify({
        "user": user.to_dict(),
        "authenticated": True
    }), 200

@auth_bp.get("/check")
def check_token():
    """Verificar si hay un token válido"""
    auth_header = request.headers.get('Authorization')
    token = JWTService.extract_token_from_header(auth_header)
    
    if not token:
        return jsonify({
            "authenticated": False,
            "user_id": None,
            "user_email": None
        }), 200
    
    # Validar el token
    payload = JWTService.decode_token(token)
    if not payload:
        return jsonify({
            "authenticated": False,
            "user_id": None,
            "user_email": None
        }), 200
    
    return jsonify({
        "authenticated": True,
        "user_id": payload.get('user_id'),
        "user_email": payload.get('user_email')
    }), 200

@auth_bp.post("/refresh")
def refresh_token():
    """Refrescar token de acceso usando refresh token"""
    data = request.get_json() or {}
    refresh_token = data.get('refresh_token')
    
    if not refresh_token:
        return jsonify({"error": "Refresh token requerido"}), 400
    
    # Validar el refresh token
    payload = JWTService.decode_token(refresh_token)
    if not payload or payload.get('type') != 'refresh':
        return jsonify({"error": "Refresh token inválido o expirado"}), 401
    
    # Buscar el usuario
    user = User.query.get(payload['user_id'])
    if not user or not user.is_active:
        return jsonify({"error": "Usuario no encontrado o desactivado"}), 404
    
    # Generar nuevo access token
    new_access_token = JWTService.generate_token(user.id, user.email)
    
    return jsonify({
        "access_token": new_access_token,
        "token_type": "Bearer"
    }), 200