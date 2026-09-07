from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Se importan los blueprints de las rutas
from routes.users import users_bp
from routes.products import products_bp
from routes.categories import categories_bp
from routes.orders import orders_bp
from routes.auth import auth_bp
from routes.payments import payments_bp

# Se importan los modelos para que SQLAlchemy los reconozca
from models.user import User
from models.category import Category
from models.product import Product
from models.category_product import CategoryProduct
from models.order import Order
from models.order_product import OrderProduct

from extensions import db
import config

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)
migrate = Migrate(app, db)

# Configurar CORS para permitir headers de autorización
CORS(app, 
     allow_headers=["Content-Type", "Authorization"],
     expose_headers=["Authorization"])

app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(payments_bp)

if __name__ == "__main__":
    app.run(debug=True)