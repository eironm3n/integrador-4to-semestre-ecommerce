# services/base_service.py
from extensions import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError

class BaseService:
    model = None

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, obj_id):
        return cls.model.query.get(obj_id)

    @classmethod
    def create(cls, data):
        try:
            name = data.get('name')
            slug = data.get('slug')

            if slug:
                data['slug'] = slug.lower().replace(' ', '-')
            elif name:
                data['slug'] = name.lower().replace(' ', '-')
            obj = cls.model()
            obj.update(data)
            obj.save()
            return obj
        except IntegrityError as e:
            db.session.rollback()
            # Handle foreign key constraint failures
            if "foreign key constraint fails" in str(e.orig):
                raise ValueError("Referencia inválida: el registro referenciado no existe")
            # Handle unique constraint failures
            elif "UNIQUE constraint failed" in str(e.orig) or "Duplicate entry" in str(e.orig):
                raise ValueError("Ya existe un registro con esos datos")
            else:
                raise ValueError(f"Error de integridad de datos: {str(e.orig)}")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error de base de datos: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error inesperado: {str(e)}")

    @classmethod
    def update(cls, obj_id, data):
        obj = cls.get_by_id(obj_id)
        if not obj:
            return None
        obj.update(data)
        return obj

    @classmethod
    def delete(cls, obj_id):
        obj = cls.get_by_id(obj_id)
        if not obj:
            return False
        obj.delete()
        return True
