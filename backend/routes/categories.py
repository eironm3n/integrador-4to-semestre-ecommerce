# routes/categories.py
from flask import Blueprint, jsonify, request
from services.category_service import CategoryService

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")

@categories_bp.get("/")
def get_categories_route():
    categories = CategoryService.get_all()
    return jsonify([c.to_dict() for c in categories])

@categories_bp.get("/<int:category_id>")
def get_category_route(category_id):
    category = CategoryService.get_by_id(category_id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify(category.to_dict())

@categories_bp.get("with_products/")
def get_categories_route_with_products():
    categories = CategoryService.get_all_with_products()
    return jsonify([c.to_dict(include_relationships=True) for c in categories])

@categories_bp.get("with_products/<int:category_id>")
def get_category_route_with_products(category_id):
    category = CategoryService.get_by_id_with_products(category_id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify(category.to_dict(include_relationships=True))

@categories_bp.post("/")
def create_category_route():
    data = request.get_json() or {}
    category = CategoryService.create(data)
    if not category:
        return jsonify({"Error": "Una categoria con ese nombre ya existe"}), 409
    
    return jsonify({"message": "Categoría creada", "category": category.to_dict()}), 201
    
    

@categories_bp.put("/<int:category_id>")
def update_category_route(category_id):
    data = request.get_json() or {}
    category = CategoryService.update(category_id, data)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify({"message": "Categoría actualizada", "category": category.to_dict()})

@categories_bp.delete("/<int:category_id>")
def delete_category_route(category_id):
    success = CategoryService.delete(category_id)
    if not success:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify({"message": "Categoría eliminada"})

@categories_bp.get("/featured")
def get_main_categories_route():
    categories = CategoryService.get_main_categories()
    return jsonify([c.to_dict(include_relationships=True) for c in categories])