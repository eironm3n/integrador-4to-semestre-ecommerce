from functools import wraps
from flask import request, jsonify, g
from services.jwt_service import JWTService

def login_required(f):
    """Decorador para rutas que requieren autenticación JWT"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        token = JWTService.extract_token_from_header(auth_header)
        
        if not token:
            return jsonify({"error": "Token de autorización requerido"}), 401
        
        # Validar el token
        payload = JWTService.decode_token(token)
        if not payload:
            return jsonify({"error": "Token inválido o expirado"}), 401
        
        # Guardar información del usuario en el contexto de la aplicación
        g.current_user_id = payload['user_id']
        g.current_user_email = payload['user_email']
        g.token_payload = payload
        
        return f(*args, **kwargs)
    return decorated_function

def get_current_user_id():
    """Obtener el ID del usuario actual del token JWT"""
    return getattr(g, 'current_user_id', None)

def get_current_user_email():
    """Obtener el email del usuario actual del token JWT"""
    return getattr(g, 'current_user_email', None)

def get_token_payload():
    """Obtener el payload completo del token JWT"""
    return getattr(g, 'token_payload', None)

def is_authenticated():
    """Verificar si el usuario está autenticado"""
    auth_header = request.headers.get('Authorization')
    token = JWTService.extract_token_from_header(auth_header)
    
    if not token:
        return False
    
    payload = JWTService.decode_token(token)
    return payload is not None