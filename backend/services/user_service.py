# services/user_service.py
from models.user import User
from services.base_service import BaseService
from extensions import db

class UserService(BaseService):
    model = User
    
    @classmethod
    def create_user_with_password(cls, data):
        """Crear un usuario con contraseña hasheada"""
        if not data.get('password'):
            raise ValueError("Password es requerido")
        
        user = cls.model(
            name=data.get('name'),
            email=data.get('email')
        )
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        return user
    
    @classmethod
    def authenticate(cls, email, password):
        """Autenticar usuario con email y contraseña"""
        user = cls.model.query.filter_by(email=email).first()
        if user and user.check_password(password) and user.is_active:
            return user
        return None
    
    @classmethod
    def change_password(cls, user_id, old_password, new_password):
        """Cambiar contraseña de usuario"""
        user = cls.get_by_id(user_id)
        if not user:
            return None
        
        if not user.check_password(old_password):
            raise ValueError("Contraseña actual incorrecta")
        
        user.set_password(new_password)
        db.session.commit()
        return user