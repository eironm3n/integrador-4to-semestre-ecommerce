# routes/orders.py
from flask import Blueprint, jsonify, request
from models.order_product import OrderProduct
from services.order_service import OrderService
from services.user_service import UserService

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

@orders_bp.get("/")
def get_orders_route():
    orders = OrderService.get_all()
    return jsonify([o.to_dict() for o in orders])

@orders_bp.get("/<int:order_id>")
def get_order_route(order_id):
    order = OrderService.get_by_id(order_id)
    if not order:
        return jsonify({"error": "Orden no encontrada"}), 404
    return jsonify(order.to_dict())

@orders_bp.put("/<int:order_id>")
def update_order_route(order_id):
    data = request.get_json() or {}
    order = OrderService.get_by_id(order_id)
    if not order:
        return jsonify({"error": "Orden no encontrada"}), 404
    if getattr(order, "status", None) != "active":
        return jsonify({"error": "Solo se pueden editar órdenes activas"}), 400
    data.pop("user_id", None)
    data.pop("date", None)
    data.pop("status", None)
    updated_order = OrderService.update(order_id, data)
    return jsonify({"message": "Orden actualizada", "order": updated_order.to_dict()})

@orders_bp.delete("/<int:order_id>")
def delete_order_route(order_id):
    success = OrderService.delete(order_id)
    if not success:
        return jsonify({"error": "Orden no encontrada"}), 404
    return jsonify({"message": "Orden eliminada"})

@orders_bp.get("/by-user/<int:user_id>")
def get_orders_by_user_route(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    orders = OrderService.get_all_by_user(user_id)
    return jsonify([o.to_dict(include_relationships=True) for o in orders])

@orders_bp.get("/by-user/<int:user_id>/active")
def get_active_order_by_user_route(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    order = OrderService.get_active_by_user(user_id)
    if not order:
        return jsonify({"message": "No active order"}), 200
    return jsonify(order.to_dict(include_relationships=True))

@orders_bp.patch("/<int:order_id>/change-status")
def change_status_route(order_id):
    data = request.get_json() or {}
    new_status = data.get("status")
    if not new_status:
        return jsonify({"error": "El nuevo status es requerido"}), 400
    order = OrderService.get_by_id(order_id)
    if not order:
        return jsonify({"error": "Orden no encontrada"}), 404
    updated_order = OrderService.update(order_id, {"status": new_status})
    return jsonify({"message": "Status actualizado", "order": updated_order.to_dict()})

@orders_bp.patch("/by-user/<int:user_id>/active/change-product-amount")
def change_product_amount_route(user_id):
    data = request.get_json()
    product_id = data.get("product_id")
    new_quantity = data.get("quantity")

    if not product_id or new_quantity is None:
        return jsonify({"error": "product_id y quantity son requeridos"}), 400

    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    order = OrderService.get_active_by_user(user_id)
    if not order:
        return jsonify({"error": "No hay una orden activa"}), 404

    order_product = (
        OrderProduct.query
        .filter_by(order_id=order.id, product_id=product_id)
        .first()
    )

    if not order_product:
        return jsonify({"error": "El producto no está en la orden activa"}), 404

    oldPrice = order_product.product.price * order_product.quantity * -1
    newPrice = order_product.product.price * new_quantity
    
    order_product.update({"quantity": new_quantity})
    order.update({"total": order.total + (oldPrice + newPrice)})

    return jsonify({
        "message": "Cantidad actualizada correctamente",
        "order_product": {
            "product_id": order_product.product_id,
            "order_id": order_product.order_id,
            "quantity": order_product.quantity
        }
    }), 200