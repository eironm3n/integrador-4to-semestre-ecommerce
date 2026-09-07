# models/category_product.py
from extensions import db

class CategoryProduct(db.Model):
    __tablename__ = 'category_products'

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)