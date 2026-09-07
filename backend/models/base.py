# models/base.py
from extensions import db
from sqlalchemy.orm import class_mapper, RelationshipProperty

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def to_dict(self, include_relationships=False):
        # Columnas básicas
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        if include_relationships:
            mapper = class_mapper(self.__class__)
            for name, prop in mapper.all_orm_descriptors.items():
                # Solo relaciones
                if isinstance(getattr(self.__class__, name).property, RelationshipProperty):
                    related = getattr(self, name)
                    if related is None:
                        result[name] = None
                    elif isinstance(related, list):
                        result[name] = [r.to_dict() for r in related]
                    else:
                        result[name] = related.to_dict()
        return result

    def update(self, data):
        for key in data:
            if hasattr(self, key):
                setattr(self, key, data[key])
        db.session.commit()
                
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()