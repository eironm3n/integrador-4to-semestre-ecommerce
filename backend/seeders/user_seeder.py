from app import db
from models.user import User

def run():
    # Limpiar usuarios existentes (las foreign keys ya se limpiaron en seed.py)
    try:
        User.query.delete()
        db.session.commit()
        print("   - Usuarios existentes eliminados")
    except Exception as e:
        print(f"   - Advertencia: No se pudieron eliminar usuarios existentes: {e}")
        db.session.rollback()
    
    # Lista de usuarios con contraseñas
    users_data = [
        {"name": "Lauti", "email": "lauti@example.com", "password": "password123"},
        {"name": "Aron", "email": "aron@example.com", "password": "password123"},
        {"name": "Dilan", "email": "dilan@example.com", "password": "password123"},
        {"name": "Eli", "email": "eli@example.com", "password": "password123"},
        {"name": "Fran", "email": "fran@example.com", "password": "password123"},
        {"name": "Juan", "email": "juan@example.com", "password": "password123"},
        {"name": "Ro", "email": "ro@example.com", "password": "password123"},
        {"name": "Guardini", "email": "guardini@example.com", "password": "password123"},
        {"name": "Agus", "email": "agus@example.com", "password": "password123"},
        {"name": "AgusJunior", "email": "agusjunior@example.com", "password": "password123"},
        {"name": "GuardiniJunior", "email": "guardinijunior@example.com", "password": "password123"},
        {"name": "RoJunior", "email": "rojunior@example.com", "password": "password123"},
        {"name": "JuanJunior", "email": "juanjunior@example.com", "password": "password123"},
        {"name": "FranJunior", "email": "franjunior@example.com", "password": "password123"},
        {"name": "EliJunior", "email": "elijunior@example.com", "password": "password123"},
        {"name": "DilanJunior", "email": "dilanjunior@example.com", "password": "password123"},
        {"name": "AronJunior", "email": "aronjunior@example.com", "password": "password123"},
        {"name": "LautiJunior", "email": "lautijunior@example.com", "password": "password123"},
        {"name": "Admin", "email": "admin@enigma.com", "password": "admin123"},  # Usuario admin
    ]
    
    # Crear usuarios con contraseñas hasheadas
    for user_data in users_data:
        user = User(
            name=user_data["name"],
            email=user_data["email"]
        )
        user.set_password(user_data["password"])
        db.session.add(user)
    
    db.session.commit()
    print(f"✅ Users seed OK - {len(users_data)} usuarios creados")
    print("📧 Usuarios de prueba:")
    for user_data in users_data:
        print(f"   - {user_data['email']} / {user_data['password']}")