from app import db
from models.category import Category

def run():
    rows = [
        Category(
            name="Plantas de interior",
            slug="plantas-de-interior",
            is_featured=True
        ),
        Category(
            name="Plantas suculentas",
            slug="plantas-suculentas",
            is_featured=True
        ),
        Category(
            name="Macetas",
            slug="macetas",
            is_featured=False
        ),
        Category(
            name="Sustratos y fertilizantes",
            slug="sustratos-y-fertilizantes",
            is_featured=False
        ),
        Category(
            name="Plantas de sombra",
            slug="plantas-de-sombra",
            is_featured=True
        ),
        Category(
            name="Plantas artificiales",
            slug="plantas-artificiales",
            is_featured=False
        ),
        # --- nuevas categorías basadas en los productos agregados ---

        Category(
            name="Bulbos y flores de temporada",
            slug="bulbos-y-flores-de-temporada",
            is_featured=False
        ),
        Category(
            name="Árboles y arbustos decorativos",
            slug="arboles-y-arbustos-decorativos",
            is_featured=True
        ),
        Category(
            name="Plantas aromáticas y eucaliptos",
            slug="plantas-aromaticas-y-eucaliptos",
            is_featured=False
        ),
        Category(
            name="Hierbas para gatos",
            slug="hierbas-para-gatos",
            is_featured=False
        ),
        Category(
            name="Plantas acuáticas",
            slug="plantas-acuaticas",
            is_featured=False
        ),
        Category(
            name="Bonsáis",
            slug="bonsais",
            is_featured=True
        ),
        Category(
            name="Plantas trepadoras",
            slug="plantas-trepadoras",
            is_featured=False
        ),
                Category(
            name="Flores secas",
            slug="flores-secas",
            is_featured=False
        ),
        Category(
            name="Bulbos de flores",
            slug="bulbos-de-flores",
            is_featured=True
        ),
                Category(
            name="Plantas con flor de interior",
            slug="plantas-con-flor-de-interior",
            is_featured=True
        ),
        Category(
            name="Orquídeas",
            slug="orquideas",
            is_featured=True
        ),
        Category(
            name="Palmeras de interior",
            slug="palmeras-de-interior",
            is_featured=True
        ),
        Category(
            name="Cactus",
            slug="cactus",
            is_featured=False
        ),
        Category(
            name="Plantas tropicales",
            slug="plantas-tropicales",
            is_featured=True
        )

    ]

    Category.query.delete()
    db.session.commit()
    
    db.session.bulk_save_objects(rows)
    db.session.commit()
    print("Categories seed OK")