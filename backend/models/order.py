# models/order.py
from extensions import db
from models.base import BaseModel

class Order(BaseModel):
    __tablename__ = "orders"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())
    status = db.Column(db.String(50), nullable=False, default='active')
    total = db.Column(db.Float, nullable=False, default=0)
    products = db.relationship(
        "Product",
        secondary="order_products",
        back_populates="orders",
        overlaps="order_products,product"
    )
    user = db.relationship(
        "User",
        back_populates="orders"
    )