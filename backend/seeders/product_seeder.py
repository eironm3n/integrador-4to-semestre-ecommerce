from app import db
from models.product import Product

def run():
    rows = [
        Product(
            name="Ficus Lyrata",
            price="8500.00",
            description="Planta de interior popular conocida como Higuera de hojas de violín. Ideal para espacios luminosos.",
            image_url="https://florastore.com/cdn/shop/files/3313211_Productimage_01_SQ_c5567bfa-4772-47cb-a2aa-bc533d84e5b7.jpg",
            size="Mediana",
            care_level="Moderado"
        ),
        Product(
            name="Monstera Deliciosa",
            price="7200.00",
            description="Planta tropical de gran follaje con hojas perforadas. Perfecta para decoración de interiores.",
            image_url="https://florastore.com/cdn/shop/files/1711701_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Bajo"
        ),
        Product(
            name="Cactus Euphorbia Ingens",
            price="2500.00",
            description="Cactus resistente de fácil cuidado, ideal para interiores y exteriores.",
            image_url="https://florastore.com/cdn/shop/files/2021171_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Bajo"
        ),
        Product(
            name="Portamacetas 3 niveles",
            price="18000.00",
            description="Un hermoso portamacetas de 3 niveles negro para plantas de interior",
            image_url="https://florastore.com/cdn/shop/files/5801001_Productimage_05_SQ.png"
        ),
        Product(
            name="Concentrado para el control de malezas",
            price="950.00",
            description="Con el Concentrado Control de Malezas Pokon, puedes eliminar rápida y fácilmente las malas hierbas anuales indeseadas, como la pamplina, el berro y la ortiga.",
            image_url="https://florastore.com/cdn/shop/files/9800002_Productimage_02_SQ.png"
        ),
        Product(
            name="Tierra fértil 10kg",
            price="2100.00",
            description="Bolsa de tierra abonada lista para macetas y jardines.",
            image_url="https://florastore.com/cdn/shop/files/9826001_Productimage_02_SQ.png"
        ),
        Product(
            name="Musa Oriental",
            price="3200.00",
            description="La planta de plátano de interior, también llamada Musa Oriental Dwarf, es originaria del sudeste asiático y Australia. Es una planta de interior tropical con hermosas hojas verdes grandes.",
            image_url="https://florastore.com/cdn/shop/files/3110121_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Alto"
        ),
        Product(
            name="Orquídea Phalaenopsis",
            price="12500.00",
            description="Orquídea elegante de flores duraderas, disponible en varios colores.",
            image_url="https://florastore.com/cdn/shop/files/3514301_Productimage_02_SQ.jpg",
            size="Chica",
            care_level="Moderado"
        ),
        Product(
            name="Suculenta mix (3 unidades)",
            price="3100.00",
            description="Pack de 3 suculentas variadas en macetas pequeñas, de bajo mantenimiento.",
            image_url="https://florastore.com/cdn/shop/files/2513003_Productimage_03_SQ.png",
            size="Chica",
            care_level="Bajo"
        ),
        Product(
            name="Eucalipto Pulverulenta (2 unidades)",
            price="4600.00",
            description="El Eucalyptus Pulverulenta Baby Blue es originario del sureste de Australia y es la comida favorita de los koalas.",
            image_url="https://florastore.com/cdn/shop/files/1530192_Productimage_02_SQ.jpg",
            size="Mediana",
            care_level="Bajo"
        ),
        Product(
            name="Orquidea Vanda",
            price="15000.00",
            description="Orquídea exótica de raíces aéreas, requiere alta humedad.",
            image_url="https://florastore.com/cdn/shop/files/5231001_Productimage_01_SQ_jo1v6g.jpg",
            size="Mediana",
            care_level="Alto"
        ),
        Product(
            name="Medinilla Magnifica",
            price="9800.00",
            description="Planta tropical con flores colgantes rosadas.",
            image_url="https://florastore.com/cdn/shop/files/7031701_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Alto"
        ),
        Product(
            name="Planta artificial kentia",
            price="8100.00",
            description="Palmera Kentia artificial de aspecto realista, sin mantenimiento.",
            image_url="https://florastore.com/cdn/shop/files/3413001_Productimage_03_SQ.jpg"
            # size y care_level se omiten (seran NULL)
        ),
        Product(
            name="Olivo artificial",
            price="9300.00",
            description="Olivo artificial decorativo para interiores.",
            image_url="https://florastore.com/cdn/shop/files/3415001_Productimage_03_SQ.jpg"
            # size y care_level se omiten (seran NULL)
        ),
        Product(
            name="Tulipa mezcla rojo y rosa",
            price="2495",
            description="Mezcla de tulipanes rojos y rosados (Tulipa Zalm y Tulipa van Eijk). Ideales para maceta o suelo. Plantar entre septiembre y diciembre; florecen en mayo. Altura aprox. 40 a 50 cm.",
            image_url="https://florastore.com/cdn/shop/files/1915080_Productimage_01_SQ.jpg"
            # size y care_level omitidos (NULL)
        ),

        Product(
            name="Tulipa Black Hero",
            price="2695.00",
            description="Tulipán doble de color púrpura muy oscuro (casi negro). Flores grandes en tallos fuertes (60 cm). Apto para maceta o suelo y excelente como flor de corte. Plantar de septiembre a diciembre; floración en mayo.",
            image_url="https://florastore.com/cdn/shop/files/1944115_Productimage_01_SQ.png"
            # size y care_level omitidos (NULL)
        ),

        Product(
            name="Acer Palmatum Starfish set de 2",
            price="5995.00",
            description="El follaje en forma de estrella de mar se torna rojo más intenso en otoño. Resistente al invierno y caducifolio. Prefiere semisombra a sol; puede ir en suelo o maceta. Podar en verano o en diciembre solo si es necesario. Altura de entrega 60 a 70 cm (maceta 19 cm).",
            image_url="https://florastore.com/cdn/shop/files/3044192_Productimage_01_SQ.png",
            size="Grande",
            care_level="Moderado"
        ),

        Product(
            name="Eucalyptus pulverulenta Baby Blue set de 6",
            price="4595.00",
            description="Originario del sudeste de Australia; muy usado en flor cortada por sus hojas azul-gris aromáticas. Apta para interior y exterior; rusticidad moderada (proteger de heladas fuertes). Altura de entrega 25 a 40 cm (maceta 12 cm). Le gusta sol/suelo bien drenado; la poda en marzo ayuda a mantenerla compacta.",
            image_url="https://florastore.com/cdn/shop/files/3025004_Productimage_03_SQ_29fd88f9-37ad-41ff-93b4-7ea99ace9689.jpg",
            size="Mediana",
            care_level="Moderado"
        ),

        Product(
            name="Cyperus Hierba para gatos set de 6",
            price="2595.00",
            description="A los gatos les encanta y es segura para ellos; las fibras ayudan a la digestión. De riego frecuente (tolera platito con agua). Prefiere lugar luminoso y cálido, evitando sol directo. Altura de entrega 30 a 40 cm (maceta 12 cm).",
            image_url="https://florastore.com/cdn/shop/files/4211126_Productimage_02_SQ.png",
            size="Mediana",
            care_level="Bajo"
        ),
        Product(
            name="Cyperus Alternifolius set de 2",
            price="2895.00",
            description="Set de 2 Cyperus alternifolius (planta paraguas). Altura de entrega 40 a 50 cm (maceta 14 cm). Ama la luz y el riego regular; ideal para lugares luminosos. Cuidado de nivel medio.",
            image_url="https://florastore.com/cdn/shop/files/4213142_Productimage_02_SQ.jpg",
            size="Mediana",
            care_level="Moderado"
        ),

        Product(
            name="Ficus Ginseng Bonsái japonés",
            price="2095.00",
            description="Ficus microcarpa Ginseng con tronco de raíces expuestas y copa compacta. Altura 30 a 40 cm (maceta 12 cm). Prefiere semisombra y riegos moderados. Origen cultivado con poda paciente para su forma de bonsái.",
            image_url="https://florastore.com/cdn/shop/files/2358121_Productimage_01_SQ.png",
            size="Mediana",
            care_level="Moderado"
        ),

        Product(
            name="Bonsái con sistema de agua Easy Care Buddha",
            price="4295.00",
            description="Arreglo de bonsái real con fuente y figura Buddha. Sistema Easy Care que facilita el riego (1 vez por semana). Altura 25 a 35 cm; ideal para interiores luminosos en semisombra.",
            image_url="https://florastore.com/cdn/shop/files/2363001_Atmosphere_02_SQ_6ceca92e-7225-40c7-82fe-d5ff3842f14a.jpg",
            size="Chica",
            care_level="Moderado"
        ),

        Product(
            name="Plumbago auriculata Set de 3",
            price="2295.00",
            description="Trepadora de larga floración con abundantes flores azules. Apta para maceta o suelo, proteger de heladas fuertes. Altura de entrega 25 a 40 cm (maceta 9 cm). Cuidado de nivel medio.",
            image_url="https://florastore.com/cdn/shop/files/2560003_Productimage_01_SQ.jpg"
            # size y care_level se omiten (seran NULL)
        ),

        Product(
            name="Parthenocissus Hiedra virgen",
            price="3695.00",
            description="Trepadora autoadherente de crecimiento rápido y color otoñal rojo intenso. Muy rústica (hasta 30 °C). Altura de entrega 25 a 40 cm (maceta 9 cm). Cuidado de nivel medio.",
            image_url="https://florastore.com/cdn/shop/files/2552006_Productimage_01_SQ.png",
            size="Mediana",
            care_level="Moderado"
        ),
        # Nuevos 20 productos

                # --- FLORES SECAS ---
        Product(
            name="Ramo Protea Pendula Rojo 5 tallos",
            price="2945.00",
            description="Ramo de 5 proteas pendula rojas secas. Ideal para jarrones decorativos; tonos cálidos y textura llamativa.",
            image_url="https://florastore.com/cdn/shop/files/4603008_Productimage_01_SQ.png"
        ),
        Product(
            name="Bouquet Scandinavian Dream",
            price="3095.00",
            description="Bouquet listo para usar con luffa, palm spear, broom grass, palm sun, oat grass, reed cone y babla. Altura aprox. 60 cm.",
            image_url="https://florastore.com/cdn/shop/files/4602007_Productimage_01_SQ_iwrhob.png"
        ),
        Product(
            name="Bouquet Trendy Comfort",
            price="3045.00",
            description="Bouquet de estilo natural, listo para colocar en jarrón. Colores cálidos y mezcla de texturas para interiores acogedores.",
            image_url="https://florastore.com/cdn/shop/files/4602002_Productimage_01_SQ_5xrkh2.png"
        ),
        Product(
            name="Bouquet Trendy Cool",
            price="3045.00",
            description="Bouquet de estética moderna con mezcla de tallos secos y tonos sobrios. Ideal para ambientes minimalistas.",
            image_url="https://florastore.com/cdn/shop/files/4602002_Productimage_01_SQ_7mx907.png"
        ),
        Product(
            name="Protea compacta 10 tallos",
            price="3395.00",
            description="Set de 10 proteas compactas secas con cabezas densas y color intenso. Perfectas para arreglos duraderos.",
            image_url="https://florastore.com/cdn/shop/files/4603007_Productimage_01_SQ.png"
        ),

        # --- BULBOS ---
        Product(
            name="Galanthus Elwesii x50",
            price="2995.00",
            description="Bulbos de campanilla de nieve (x50). Flores blancas muy tempranas de fin de invierno/primavera. Altura aprox. 10 a 15 cm.",
            image_url="https://florastore.com/cdn/shop/files/1928050_Atmosphere_01_SQ.jpg"
        ),
        Product(
            name="Ranunculus mezcla x40",
            price="1899.00",
            description="Mezcla de 40 bulbos de ranúnculo en varios colores. Floración prolongada en verano; excelentes también como flor de corte.",
            image_url="https://florastore.com/cdn/shop/files/1902940_Productimage_01_SQ.png"
        ),
        Product(
            name="Tulipa Dreamer x15",
            price="2695.00",
            description="Tulipanes Dreamer de flor doble tipo peonía en rosa suave. Altura aprox. 40 a 45 cm. Aptos para macetas o canteros.",
            image_url="https://florastore.com/cdn/shop/files/1913015_Productimage_01_SQ.png"
        ),
        Product(
            name="Crocus Ruby Giant x200",
            price="3495.00",
            description="Crocus de floración muy temprana en púrpura intenso. Siembra otoñal. Altura aprox. 10 a 12 cm, ideal en grupos.",
            image_url="https://florastore.com/cdn/shop/files/1930200_Productimage_01_SQ.png"
        ),
        Product(
            name="Hyacinthus Blue Trophy x25",
            price="3595.00",
            description="Jacintos Blue Trophy de azul profundo y fragancia destacada. Altura aprox. 20 a 30 cm; plantación otoñal.",
            image_url="https://florastore.com/cdn/shop/files/1910025_Productimage_01_SQ.png"
        ),
                # --- BLOEIENDE KAMERPLANTEN / PLANTAS CON FLOR DE INTERIOR ---
        Product(
            name="Medinilla magnifica 2 unidades",
            price="3795.00",
            description="Set de 2 Medinilla magnifica con racimos colgantes. Maceta 17 cm, altura 40 a 50 cm. Prefiere luz indirecta y riego moderado.",
            image_url="https://florastore.com/cdn/shop/files/4220172_Product-image_02_SQ.jpg",
            size="Mediana",
            care_level="Moderado"
        ),
        Product(
            name="Medinilla magnifica Flamenco",
            price="3095.00",
            description="Variedad Flamenco con flores rosadas en racimos y hojas brillantes. Ideal en interior luminoso sin sol directo.",
            image_url="https://florastore.com/cdn/shop/files/7031701_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Moderado"
        ),
        Product(
            name="Gardenia jasminoides",
            price="1999.00",
            description="Gardenia de flor blanca y perfume intenso. Luz brillante sin sol directo, riego regular con poca cal.",
            image_url="https://florastore.com/cdn/shop/files/4512131_Atmosphere_02_SQ_MJ.png",
            size="Chica",
            care_level="Moderado"
        ),

        # --- KAMERPLANTEN / PLANTAS DE INTERIOR ---
        Product(
            name="Iresine herbstii Red",
            price="1999.00",
            description="Follaje rojo intenso (beefsteak plant). Prefiere luz brillante sin sol directo y sustrato siempre apenas húmedo.",
            image_url="https://florastore.com/cdn/shop/files/4507131_Productimage_02_SQ.jpg",
            size="Chica",
            care_level="Moderado"
        ),
        Product(
            name="Crassula ovata Sunset",
            price="6995.00",
            description="Suculenta tipo árbol de jade con tonos amarillos/rojizos al sol. Riego escaso; dejar secar entre riegos.",
            image_url="https://florastore.com/cdn/shop/files/8611301_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Bajo"
        ),
        Product(
            name="Mini cactus",
            price="2795.00",
            description="Pack de 12 mini cactus surtidos. Muy fáciles de cuidar; requieren poca agua y buena luz.",
            image_url="https://florastore.com/cdn/shop/files/4920512_Productimage_02_SQ.jpg",
            size="Chica",
            care_level="Bajo"
        ),

        # --- ORQUÍDEAS ---
        Product(
            name="Vanda Magic talle XXL",
            price="6495.00",
            description="Orquídea Vanda de raíces aéreas y floración azul intensa. Requiere mucha luz (sin sol directo) y baños de agua semanales.",
            image_url="https://florastore.com/cdn/shop/files/5221001_Productimage_01_SQ_e098abd3-07da-4b42-a639-b772b5f2ced9.jpg",
            size="Grande",
            care_level="Alto"
        ),
        Product(
            name="Vanda azul talle L",
            price="5595.00",
            description="Orquídea Vanda azul (talle L). Crecimiento sin sustrato con raíces aéreas; riegos por inmersión.",
            image_url="https://florastore.com/cdn/shop/files/5231001_Productimage_01_SQ_jo1v6g.jpg",
            size="Mediana",
            care_level="Alto"
        ),

        # --- PALMERAS Y TROPICALES ---
        Product(
            name="Dypsis lutescens Areca Dorada",
            price="3595.00",
            description="Palmera Areca de interior. Aire purificadora; luz brillante sin sol directo y humedad ambiental moderada.",
            image_url="https://florastore.com/cdn/shop/files/3510211_Productimage_02_SQ.jpg",
            size="Grande",
            care_level="Moderado"
        ),
        Product(
            name="Musa cavendish Banano Enano",
            price="2550.00",
            description="Banano de interior de gran porte y look tropical. Mucha luz y riego frecuente manteniendo el sustrato húmedo.",
            image_url="https://florastore.com/cdn/shop/files/3532101_Productimage_03_SQ.png",
            size="Grande",
            care_level="Alto"
        )

    ]

    Product.query.delete()
    db.session.commit()

    db.session.bulk_save_objects(rows)
    db.session.commit()
    print("Products seed OK")


