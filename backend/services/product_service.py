# services/product_service.py
from models.product import Product
from services.base_service import BaseService
from models.order_product import OrderProduct
from models.category import Category
from sqlalchemy import and_, or_

class ProductService(BaseService):
    model = Product
    
    def update_or_create_order_product(product_id, order_id, quantity):
        # Buscar si ya existe el producto en la orden
        order_product = OrderProduct.query.filter_by(
            product_id=product_id,
            order_id=order_id
        ).first()

        if order_product:
            # Si ya existe, sumar la cantidad
            order_product.quantity += quantity
        else:
            # Si no existe, crear uno nuevo
            order_product = OrderProduct(
                product_id=product_id,
                order_id=order_id,
                quantity=quantity
            )

        # Guardar cambios
        order_product.save()
        return order_product

    # sobreescribir el metodo get_all del BaseService solo para los productos
    @classmethod
    def get_all(cls, category_id=None, search_query=None, min_price=None, max_price=None, size=None, care=None, modo=None):
        query = cls.model.query
        # lista para guardar todas las condiciones de filtro
        filtros = []

        if category_id:
            try:
                ids = [int(i) for i in category_id.split(',')]
                query = query.join(Product.categories)
                filtros.append(Category.id.in_(ids))
            except ValueError:
                pass
        
        if search_query:
            terminos = [term.strip() for term in search_query.split(',')]
            condiciones_busqueda = []
            for term in terminos:
                condiciones_busqueda.append(cls.model.name.ilike(f'%{term}%'))
                condiciones_busqueda.append(cls.model.description.ilike(f'%{term}%'))
            filtros.append(or_(*condiciones_busqueda))

        if min_price is not None:
            try:
                filtros.append(cls.model.price >= float(min_price))
            except ValueError:
                pass
        if max_price is not None:
            try:
                filtros.append(cls.model.price <= float(max_price))
            except ValueError:
                pass

        if size:
            valores = [val.strip() for val in size.split(',')]
            filtros.append(cls.model.size.in_(valores))

        if care:
            valores = [val.strip() for val in care.split(',')]
            filtros.append(cls.model.care_level.in_(valores))

        # aplicacion de filtros
        if filtros:
            if modo == 'or':
                query = query.filter(or_(*filtros))
            else:  # por defecto es AND
                query = query.filter(and_(*filtros))

        return query.all()
