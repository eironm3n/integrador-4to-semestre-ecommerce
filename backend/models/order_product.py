# models/order_product.py
from extensions import db
from models.base import BaseModel

class OrderProduct(BaseModel):
    __tablename__ = 'order_products'

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    product = db.relationship('Product', backref='order_products', overlaps="orders")
    order = db.relationship('Order', backref='order_products', overlaps="orders,products")