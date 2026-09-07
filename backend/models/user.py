# models/user.py
from extensions import db
from models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    
    # Relación con órdenes
    orders = db.relationship(
        "Order", 
        back_populates="user", 
        lazy=True
    )
    
    def set_password(self, password):
        """Hashea la contraseña y la almacena"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica si la contraseña proporcionada es correcta"""
        return check_password_hash(self.password_hash, password)
    
    def update_last_login(self):
        """Actualiza la fecha de último login"""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def to_dict(self):
        """Convierte el usuario a diccionario (sin incluir la contraseña)"""
        data = super().to_dict()
        data.pop('password_hash', None)
        return data
