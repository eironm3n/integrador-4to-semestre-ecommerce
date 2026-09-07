# services/category_service.py
from models.category import Category
from services.base_service import BaseService
from extensions import db
from sqlalchemy.orm import joinedload

class CategoryService(BaseService):
    model = Category
    
    @classmethod
    def get_all_with_products(cls):
        return cls.model.query.options(joinedload(cls.model.products)).order_by(cls.model.position.asc()).all()
    
    @classmethod
    def get_by_id_with_products(cls, cat_id):
        return cls.model.query.options(joinedload(cls.model.products)).filter_by(id=cat_id).first()
    
    @classmethod
    def get_main_categories(cls):
        return cls.model.query.options(joinedload(cls.model.products)).filter_by(is_featured=True).order_by(cls.model.position.asc()).all()
