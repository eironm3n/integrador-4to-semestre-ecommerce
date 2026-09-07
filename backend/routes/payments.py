# routes/payments.py
from flask import Blueprint, jsonify, request
from services.mercadopago_service import MercadoPagoService
from services.order_service import OrderService

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

@payments_bp.post("/create")
def create_payment_route():
    data = request.json
    user_id = data.get("user_id")
    order_id = data.get("order_id")

    if not user_id or not order_id:
        return jsonify({"error": "user_id y order_id son requeridos"}), 400

    order = OrderService.get_active_by_id(order_id, user_id)
    if not order:
        return jsonify({"error": "Orden no encontrada, inactiva o no pertenece al usuario"}), 404

    try:
        payment_url = MercadoPagoService.create_payment_link(order.total, external_reference=order.id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "order_id": order.id,
        "payment_url": payment_url
    })

# --- Callbacks integrados ---
@payments_bp.get("/success")
def payment_success():
    order_id = request.args.get("external_reference")
    if not order_id:
        return "Falta external_reference", 400

    order = OrderService.get_by_id(order_id)
    if order:
        order.status = "paid"
        order.save()
    return f"Pago exitoso de la orden {order_id}"

@payments_bp.get("/failure")
def payment_failure():
    order_id = request.args.get("external_reference")
    if order_id:
        order = OrderService.get_by_id(order_id)
        if order:
            order.status = "failed"
            order.save()
    return f"Pago fallido de la orden {order_id}"

@payments_bp.get("/pending")
def payment_pending():
    order_id = request.args.get("external_reference")
    if order_id:
        order = OrderService.get_by_id(order_id)
        if order:
            order.status = "pending"
            order.save()
    return f"Pago pendiente de la orden {order_id}"
