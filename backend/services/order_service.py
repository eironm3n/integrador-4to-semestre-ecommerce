# services/order_service.py
from sqlalchemy import desc
from models.order import Order
from services.base_service import BaseService
from sqlalchemy.orm import joinedload

class OrderService(BaseService):
    model = Order
    
    @classmethod
    def get_all_by_user(cls, user_id):
        exists = cls.model.query.filter_by(user_id=user_id).with_entities(cls.model.id).first()
        if not exists:
            return []
        return cls.model.query.options(
            joinedload(cls.model.products),
            joinedload(cls.model.user)
        ).filter_by(user_id=user_id).order_by(desc(cls.model.id)).all()

    @classmethod
    def get_active_by_user(cls, user_id):
        exists = cls.model.query.filter_by(user_id=user_id).with_entities(cls.model.id).first()
        if not exists:
            return None
        return cls.model.query.options(
            joinedload(cls.model.products),
            joinedload(cls.model.user)
        ).filter_by(user_id=user_id, status='active').first()
        
    @classmethod
    def get_active_by_id(cls, order_id, user_id):
        return (
            cls.model.query.options(
                joinedload(cls.model.products),
                joinedload(cls.model.user)
            )
            .filter_by(id=order_id, user_id=user_id, status="active")
            .first()
        )