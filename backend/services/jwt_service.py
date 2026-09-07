# services/jwt_service.py
import jwt
from datetime import datetime, timedelta
from flask import current_app
import config

class JWTService:
    # Lista negra de tokens (en producción usar Redis o base de datos)
    blacklisted_tokens = set()
    
    @staticmethod
    def generate_token(user_id, user_email):
        """Generar un token JWT para el usuario"""
        payload = {
            'user_id': user_id,
            'user_email': user_email,
            'exp': datetime.utcnow() + timedelta(hours=24),  # Token válido por 24 horas
            'iat': datetime.utcnow(),  # Issued at
            'type': 'access'
        }
        
        token = jwt.encode(
            payload, 
            config.SECRET_KEY, 
            algorithm='HS256'
        )
        
        return token
    
    @staticmethod
    def generate_refresh_token(user_id):
        """Generar un refresh token (válido por más tiempo)"""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=30),  # Refresh token válido por 30 días
            'iat': datetime.utcnow(),
            'type': 'refresh'
        }
        
        token = jwt.encode(
            payload, 
            config.SECRET_KEY, 
            algorithm='HS256'
        )
        
        return token
    
    @staticmethod
    def decode_token(token):
        """Decodificar y validar un token JWT"""
        try:
            # Verificar si el token está en la lista negra
            if token in JWTService.blacklisted_tokens:
                return None
            
            payload = jwt.decode(
                token, 
                config.SECRET_KEY, 
                algorithms=['HS256']
            )
            
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token expirado
        except jwt.InvalidTokenError:
            return None  # Token inválido
    
    @staticmethod
    def blacklist_token(token):
        """Agregar token a la lista negra (para logout)"""
        JWTService.blacklisted_tokens.add(token)
    
    @staticmethod
    def is_token_blacklisted(token):
        """Verificar si un token está en la lista negra"""
        return token in JWTService.blacklisted_tokens
    
    @staticmethod
    def extract_token_from_header(auth_header):
        """Extraer token del header Authorization"""
        if not auth_header:
            return None
        
        try:
            # Formato esperado: "Bearer <token>"
            scheme, token = auth_header.split(' ', 1)
            if scheme.lower() != 'bearer':
                return None
            return token
        except ValueError:
            return None