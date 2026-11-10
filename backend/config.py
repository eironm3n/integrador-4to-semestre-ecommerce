import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "proyecto_db")
DB_PORT = os.getenv("DB_PORT", "3306")

# Configuración de seguridad
# SECRET_KEY firma los tokens JWT: si fuera un valor conocido, cualquiera podría fabricar un token válido.
# En producción es obligatoria. En desarrollo (FLASK_DEBUG=1), si falta se usa una aleatoria por proceso
# (las sesiones se pierden al reiniciar el servidor).
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    if os.getenv("FLASK_DEBUG", "").lower() in ("1", "true"):
        import secrets
        import warnings

        SECRET_KEY = secrets.token_urlsafe(48)
        warnings.warn("SECRET_KEY no está definida: se usa una clave temporal (solo para desarrollo).", stacklevel=1)
    else:
        raise RuntimeError(
            "Falta la variable de entorno SECRET_KEY. Generá una con: "
            'python -c "import secrets; print(secrets.token_urlsafe(48))"'
        )

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False