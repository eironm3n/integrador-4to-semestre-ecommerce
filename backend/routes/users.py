# routes/users.py
from flask import Blueprint, jsonify, request
from services.user_service import UserService
from middlewares.auth_middleware import login_required, get_current_user_id

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.get("/")
def get_users_route():
    users = UserService.get_all()
    return jsonify([u.to_dict() for u in users])

@users_bp.get("/<int:user_id>")
def get_user_route(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.to_dict())

@users_bp.post("/")
def create_user_route():
    data = request.get_json() or {}
    user = UserService.create(data)
    return jsonify({"message": "Usuario creado", "user": user.to_dict()}), 201

@users_bp.put("/<int:user_id>")
def update_user_route(user_id):
    data = request.get_json() or {}
    user = UserService.update(user_id, data)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario actualizado", "user": user.to_dict()})

@users_bp.delete("/<int:user_id>")
def delete_user_route(user_id):
    success = UserService.delete(user_id)
    if not success:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado"})

@users_bp.post("/change-password")
@login_required
def change_password_route():
    """Cambiar contraseña del usuario actual"""
    data = request.get_json() or {}
    
    if not data.get('old_password') or not data.get('new_password'):
        return jsonify({"error": "old_password y new_password son requeridos"}), 400
    
    user_id = get_current_user_id()
    
    try:
        user = UserService.change_password(
            user_id, 
            data['old_password'], 
            data['new_password']
        )
        return jsonify({"message": "Contraseña actualizada exitosamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error al cambiar contraseña"}), 500
