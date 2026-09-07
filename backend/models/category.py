# models/category.py
from extensions import db
from models.base import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"
    
    name = db.Column(db.String(120), nullable=False, unique=True)
    slug = db.Column(db.String(120), nullable=False, unique=True)
    is_featured = db.Column(db.Boolean, default=False)
    position = db.Column(db.Integer, nullable=False, default=0)

    products = db.relationship(
        "Product",
        secondary="category_products",
        back_populates="categories"
    )