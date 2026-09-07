# seed_category_product.py
from extensions import db
from models.category import Category
from models.product import Product
from models.category_product import CategoryProduct

def run():
    category_products_map = {
        "arboles-y-arbustos-decorativos": [
            "Acer Palmatum Starfish set de 2",
            "Plumbago auriculata Set de 3"
        ],
        "bonsais": [
            "Ficus Ginseng Bonsái japonés",
            "Bonsái con sistema de agua Easy Care Buddha"
        ],
        "bulbos-de-flores": [
            "Tulipa mezcla rojo y rosa",
            "Tulipa Black Hero",
            "Galanthus elwesii (x50), Bulbos de campanilla de nieve",
            "Ranunculus mezcla (x40), Bulbos",
            "Tulipa Dreamer (x15), Bulbos",
            "Crocus Ruby Giant (x200), Bulbos",
            "Hyacinthus Blue Trophy (x25), Bulbos"
        ],
        "bulbos-y-flores-de-temporada": [
            "Tulipa mezcla rojo y rosa (80 bulbos)",
            "Tulipa Black Hero (15 bulbos)",
            "Galanthus Elwesii x50",
            "Ranunculus mezcla x40",
            "Tulipa Dreamer x15",
            "Crocus Ruby Giant x200",
            "Hyacinthus Blue Trophy x25"
        ],
        "cactus": [
            "Cactus Euphorbia Ingens",
            "Mini cactus"
        ],
        "flores-secas": [
            "Ramo Protea Pendula Rojo 5 tallos",
            "Bouquet Scandinavian Dream",
            "Bouquet Trendy Comfort",
            "Bouquet Trendy Cool",
            "Protea compacta 10 tallos"
        ],
        "hierbas-para-gatos": [
            "Cyperus Hierba para gatos set de 6"
        ],
        "macetas": [
            "Portamacetas 3 niveles"
        ],
        "orquideas": [
            "Orquídea Phalaenopsis",
            "Orquidea Vanda",
            "Vanda Magic talle XXL",
            "Vanda azul talle L"
        ],
        "palmeras-de-interior": [
            "Dypsis lutescens Areca Dorada"
        ],
        "plantas-acuaticas": [
            "Cyperus Alternifolius Set de 2"
        ],
        "plantas-aromaticas-y-eucaliptos": [
            "Eucalipto Pulverulenta (2 unidades)",
            "Eucalyptus pulverulenta Baby Blue set de 6"
        ],
        "plantas-artificiales": [
            "Planta artificial kentia",
            "Olivo artificial"
        ],
        "plantas-con-flor-de-interior": [
            "Orquídea Phalaenopsis",
            "Orquidea Vanda",
            "Medinilla Magnifica",
            "Medinilla magnifica (2 unidades), 17 cm, 40 a 50 cm",
            "Medinilla magnifica Flamenco, 17 cm, 55 a 60 cm",
            "Gardenia jasminoides, 13 cm, 20 a 30 cm",
            "Vanda Magic XXL, azul, 90 cm",
            "Vanda azul (talle L), 55 a 65 cm"
        ],
        "plantas-de-interior": [
            "Ficus Lyrata",
            "Monstera Deliciosa",
            "Musa Oriental",
            "Medinilla Magnifica",
            "Ficus Ginseng, Bonsái japonés",
            "Medinilla magnifica 2 unidades",
            "Medinilla magnifica Flamenco",
            "Gardenia jasminoides",
            "Iresine herbstii Red",
            "Dypsis lutescens (Areca, palmera dorada), 21 cm, 100 a 120 cm",
            "Bonsái con sistema de agua Easy Care Buddha"
        ],
        "plantas-suculentas": [
            "Cactus Euphorbia Ingens",
            "Suculenta mix (3 unidades)",
            "Crassula ovata Sunset",
            "Mini cactus, mix x12 (5,5 cm, 5 a 10 cm)"
        ],
        "plantas-trepadoras": [
            "Parthenocissus Hiedra virgen"
        ],
        "plantas-tropicales": [
            "Musa Oriental",
            "Musa cavendish (banano enano), 21 cm, 90 a 100 cm"
        ],
        "plantas-de-sombra": [
            "Musa cavendish Banano Enano"
        ],
        "sustratos-y-fertilizantes": [
            "Concentrado para el control de malezas",
            "Tierra fértil 10kg"
        ]

    }

    CategoryProduct.query.delete()
    db.session.commit()

    for cat_slug, product_names in category_products_map.items():
        category = Category.query.filter_by(slug=cat_slug).first()
        if not category:
            continue

        for prod_name in product_names:
            product = Product.query.filter_by(name=prod_name).first()
            if product:
                link = CategoryProduct(category_id=category.id, product_id=product.id)
                db.session.add(link)

    db.session.commit()
    print("CategoryProducts seed OK")