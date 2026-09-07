# seed.py
from app import app, db
from models.category_product import CategoryProduct
from models.order_product import OrderProduct
from models.order import Order
from seeders import user_seeder, product_seeder, category_seeder, category_product_seeder

if __name__ == "__main__":
    with app.app_context():
        print("🌱 Running seeders with central cleanup...")

        # --- BORRADO CENTRALIZADO EN ORDEN CORRECTO ---
        # 1. BORRAR LAS RELACIONES PRIMERO para evitar IntegrityError.
        print("   - Cleaning order_products relationships...")
        OrderProduct.query.delete()
        db.session.commit()
        
        print("   - Cleaning orders...")
        Order.query.delete()
        db.session.commit()
        
        print("   - Cleaning category_products relationships...")
        CategoryProduct.query.delete()
        db.session.commit()

        # --- EJECUCIÓN DE SEEDERS ---
        # Ahora llamamos a los seeders individuales.
        print("   - Running user_seeder...")
        user_seeder.run()
        print("   - Running category_seeder...")
        category_seeder.run() 
        print("   - Running product_seeder...")
        product_seeder.run()  
        print("   - Running category_product_seeder...")
        category_product_seeder.run() 

        print("\n✅ Seeders finished successfully!")