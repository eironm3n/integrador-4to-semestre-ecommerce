# routes/products.py
from flask import Blueprint, jsonify, request
from services.product_service import ProductService
from services.order_service import OrderService
from services.user_service import UserService

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.get("/")
def get_products_route():
    # si no se ingresan los parametros el valor es none
    category_id = request.args.get('category_id')
    search_query = request.args.get('search_query')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    size = request.args.get('size')
    care = request.args.get('care')

    # combinacion de filtros ('or' o por defecto 'and').
    modo = request.args.get('modo')

    products = ProductService.get_all(
        category_id=category_id,
        search_query=search_query,
        min_price=min_price,
        max_price=max_price,
        size=size,
        care=care,
        modo=modo
    )

    return jsonify([p.to_dict(include_relationships=True) for p in products])

@products_bp.get("/<int:product_id>")
def get_product_route(product_id):
    product = ProductService.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(product.to_dict(include_relationships=True))

@products_bp.post("/")
def create_product_route():
    data = request.get_json() or {}
    product = ProductService.create(data)
    return jsonify({"message": "Producto creado", "product": product.to_dict()}), 201

@products_bp.put("/<int:product_id>")
def update_product_route(product_id):
    data = request.get_json() or {}
    product = ProductService.update(product_id, data)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"message": "Producto actualizado", "product": product.to_dict()})

@products_bp.delete("/<int:product_id>")
def delete_product_route(product_id):
    success = ProductService.delete(product_id)
    if not success:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"message": "Producto eliminado"})

@products_bp.post("/<int:product_id>/add_to_cart")
def add_to_cart_route(product_id):
    data = request.get_json() or {}
    quantity = data.get("quantity", 1)
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Falta el parámetro user_id"}), 400

    # Verificar que el usuario existe
    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Verificar que el producto existe
    product = ProductService.get_by_id(product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    try:
        # Buscar orden activa del usuario
        order = OrderService.get_active_by_user(user_id)
        if not order:
            order = OrderService.create({"user_id": user_id, "quantity": quantity})

        # Agregar producto a la orden
        order_product = ProductService.update_or_create_order_product(product_id, order.id, quantity)
        if not order_product:
            return jsonify({"error": "No se pudo agregar el producto al carrito"}), 400
        else:
            order.update({"total": order.total + order_product.product.price * quantity})
        return jsonify({
            "message": "Producto agregado al carrito",
            "order_id": order.to_dict(),
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500
