"""Seed the database with sample data — categories, products, variants, locations."""

import asyncio
import logging
import random

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_factory
from app.models.product import Category, Product, ProductVariant
from app.models.inventory import WarehouseLocation, Inventory

logger = logging.getLogger(__name__)

# ── Categories ──────────────────────────────────────────────────────────
CATEGORIES = [
    {"name": "Koszulki", "slug": "koszulki", "description": "T-shirty, polo i koszule dla każdego"},
    {"name": "Bluzy", "slug": "bluzy", "description": "Bluzy, hoodie i bluzy z zipem"},
    {"name": "Spodnie", "slug": "spodnie", "description": "Jeansy, dresy i szorty"},
    {"name": "Buty", "slug": "buty", "description": "Sneakersy, buty sportowe i trampki"},
    {"name": "Akcesoria", "slug": "akcesoria", "description": "Czapki, plecaki i dodatki"},
]

# ── Products ────────────────────────────────────────────────────────────
PRODUCTS = [
    # ── Koszulki ──
    {
        "name": "T-Shirt Premium Cotton",
        "slug": "t-shirt-premium-cotton",
        "description": "Klasyczny bawełniany T-shirt z najwyższej jakości bawełny czesanej. Miękki, przewiewny i niezwykle trwały. Idealny na co dzień – świetnie komponuje się zarówno z jeansami, jak i spodniami chinos.",
        "price": 89.99,
        "compare_price": 109.99,
        "category": "Koszulki",
        "brand": "Mercha",
        "variants": [
            {"sku": "TSH-BIA-S",   "size": "S",  "color": "Biały"},
            {"sku": "TSH-BIA-M",   "size": "M",  "color": "Biały"},
            {"sku": "TSH-BIA-L",   "size": "L",  "color": "Biały"},
            {"sku": "TSH-BIA-XL",  "size": "XL", "color": "Biały"},
            {"sku": "TSH-CZR-S",   "size": "S",  "color": "Czarny"},
            {"sku": "TSH-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "TSH-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "TSH-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "TSH-GRN-S",   "size": "S",  "color": "Granatowy"},
            {"sku": "TSH-GRN-M",   "size": "M",  "color": "Granatowy"},
            {"sku": "TSH-GRN-L",   "size": "L",  "color": "Granatowy"},
            {"sku": "TSH-GRN-XL",  "size": "XL", "color": "Granatowy"},
        ],
    },
    {
        "name": "Polo Sport",
        "slug": "polo-sport",
        "description": "Elegancka koszulka polo z krótkim rękawem, wykonana z dzianiny pique. Zapinana na guziki z klasycznym kołnierzykiem. Doskonały wybór zarówno do biura, jak i na weekendowe wyjście.",
        "price": 129.99,
        "compare_price": 159.99,
        "category": "Koszulki",
        "brand": "Mercha",
        "variants": [
            {"sku": "PLO-BIA-S",   "size": "S",  "color": "Biały"},
            {"sku": "PLO-BIA-M",   "size": "M",  "color": "Biały"},
            {"sku": "PLO-BIA-L",   "size": "L",  "color": "Biały"},
            {"sku": "PLO-BIA-XL",  "size": "XL", "color": "Biały"},
            {"sku": "PLO-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "PLO-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "PLO-GRN-M",   "size": "M",  "color": "Granatowy"},
            {"sku": "PLO-GRN-L",   "size": "L",  "color": "Granatowy"},
            {"sku": "PLO-BRD-S",   "size": "S",  "color": "Bordowy"},
            {"sku": "PLO-BRD-M",   "size": "M",  "color": "Bordowy"},
        ],
    },
    {
        "name": "Koszula Lniana Oversize",
        "slug": "koszula-lniana-oversize",
        "description": "Luźna koszula z naturalnego lnu o oversize'owym kroju. Idealna na ciepłe dni – przewiewna i lekka. Świetnie wygląda noszona rozpięta na T-shircie lub wpuszczona w spodnie.",
        "price": 179.99,
        "compare_price": None,
        "category": "Koszulki",
        "brand": "Mercha",
        "variants": [
            {"sku": "KOS-BIA-S",   "size": "S",  "color": "Biały"},
            {"sku": "KOS-BIA-M",   "size": "M",  "color": "Biały"},
            {"sku": "KOS-BIA-L",   "size": "L",  "color": "Biały"},
            {"sku": "KOS-BIA-XL",  "size": "XL", "color": "Biały"},
            {"sku": "KOS-BEZ-S",   "size": "S",  "color": "Beżowy"},
            {"sku": "KOS-BEZ-M",   "size": "M",  "color": "Beżowy"},
            {"sku": "KOS-BEZ-L",   "size": "L",  "color": "Beżowy"},
            {"sku": "KOS-NIE-M",   "size": "M",  "color": "Jasnoniebieski"},
            {"sku": "KOS-NIE-L",   "size": "L",  "color": "Jasnoniebieski"},
        ],
    },

    # ── Bluzy ──
    {
        "name": "Bluza Z Kapturem Classic",
        "slug": "bluza-z-kapturem-classic",
        "description": "Ciepła bluza z kapturem wykonana z mięsistej dzianiny. Ściągacze przy mankietach i dole oraz kieszeń typu kangurka. Must-have w każdej szafie na chłodniejsze dni.",
        "price": 199.99,
        "compare_price": 249.99,
        "category": "Bluzy",
        "brand": "Mercha",
        "variants": [
            {"sku": "BLK-CZR-S",   "size": "S",  "color": "Czarny"},
            {"sku": "BLK-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "BLK-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "BLK-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "BLK-SZR-S",   "size": "S",  "color": "Szary"},
            {"sku": "BLK-SZR-M",   "size": "M",  "color": "Szary"},
            {"sku": "BLK-SZR-L",   "size": "L",  "color": "Szary"},
            {"sku": "BLK-GRN-M",   "size": "M",  "color": "Granatowy"},
            {"sku": "BLK-GRN-L",   "size": "L",  "color": "Granatowy"},
            {"sku": "BLK-GRN-XL",  "size": "XL", "color": "Granatowy"},
        ],
    },
    {
        "name": "Bluza Zip Premium",
        "slug": "bluza-zip-premium",
        "description": "Bluza zapinana na pełny zamek błyskawiczny. Wykonana z wysokiej jakości bawełny z domieszką poliestru dla lepszego zachowania kształtu. Idealna jako warstwa wierzchnia w chłodniejsze dni.",
        "price": 179.99,
        "compare_price": 219.99,
        "category": "Bluzy",
        "brand": "Mercha",
        "variants": [
            {"sku": "BLZ-CZR-S",   "size": "S",  "color": "Czarny"},
            {"sku": "BLZ-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "BLZ-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "BLZ-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "BLZ-SZR-M",   "size": "M",  "color": "Szary"},
            {"sku": "BLZ-SZR-L",   "size": "L",  "color": "Szary"},
            {"sku": "BLZ-ZIE-M",   "size": "M",  "color": "Zielony"},
            {"sku": "BLZ-ZIE-L",   "size": "L",  "color": "Zielony"},
            {"sku": "BLZ-ZIE-XL",  "size": "XL", "color": "Zielony"},
        ],
    },
    {
        "name": "Hoodie Oversize",
        "slug": "hoodie-oversize",
        "description": "Modna bluza w oversize'owym kroju. Luźny fason, opadające ramiona i długa linia. Wykonana z miękkiej, pętelkowej dzianiny od środka. Idealna do stylizacji streetwear.",
        "price": 219.99,
        "compare_price": None,
        "category": "Bluzy",
        "brand": "Mercha",
        "variants": [
            {"sku": "HOO-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "HOO-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "HOO-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "HOO-BEZ-M",   "size": "M",  "color": "Beżowy"},
            {"sku": "HOO-BEZ-L",   "size": "L",  "color": "Beżowy"},
            {"sku": "HOO-BEZ-XL",  "size": "XL", "color": "Beżowy"},
            {"sku": "HOO-FIO-M",   "size": "M",  "color": "Fioletowy"},
            {"sku": "HOO-FIO-L",   "size": "L",  "color": "Fioletowy"},
        ],
    },

    # ── Spodnie ──
    {
        "name": "Jeansy Slim Fit",
        "slug": "jeansy-slim-fit",
        "description": "Nowoczesne jeansy o wąskim kroju, idealnie dopasowujące się do sylwetki. Wykonane z elastycznego denimu z dodatkiem elastanu dla maksymalnego komfortu. Sprawdzą się zarówno w codziennych, jak i bardziej eleganckich stylizacjach.",
        "price": 199.99,
        "compare_price": 249.99,
        "category": "Spodnie",
        "brand": "Mercha",
        "variants": [
            {"sku": "JNS-CIE-30", "size": "30", "color": "Ciemny"},
            {"sku": "JNS-CIE-32", "size": "32", "color": "Ciemny"},
            {"sku": "JNS-CIE-34", "size": "34", "color": "Ciemny"},
            {"sku": "JNS-CIE-36", "size": "36", "color": "Ciemny"},
            {"sku": "JNS-JAS-30", "size": "30", "color": "Jasny"},
            {"sku": "JNS-JAS-32", "size": "32", "color": "Jasny"},
            {"sku": "JNS-JAS-34", "size": "34", "color": "Jasny"},
            {"sku": "JNS-CZR-30", "size": "30", "color": "Czarny"},
            {"sku": "JNS-CZR-32", "size": "32", "color": "Czarny"},
            {"sku": "JNS-CZR-34", "size": "34", "color": "Czarny"},
            {"sku": "JNS-CZR-36", "size": "36", "color": "Czarny"},
        ],
    },
    {
        "name": "Spodnie Dresowe Jogger",
        "slug": "spodnie-dresowe-jogger",
        "description": "Wygodne spodnie dresowe w stylu jogger ze ściągaczami przy kostkach. Wykonane z miękkiej bawełny z domieszką poliestru. Posiadają dwie kieszenie boczne oraz kieszeń z tyłu. Idealne do domu i na spacer.",
        "price": 129.99,
        "compare_price": None,
        "category": "Spodnie",
        "brand": "Mercha",
        "variants": [
            {"sku": "DRS-CZR-S",   "size": "S",  "color": "Czarny"},
            {"sku": "DRS-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "DRS-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "DRS-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "DRS-SZR-S",   "size": "S",  "color": "Szary"},
            {"sku": "DRS-SZR-M",   "size": "M",  "color": "Szary"},
            {"sku": "DRS-SZR-L",   "size": "L",  "color": "Szary"},
            {"sku": "DRS-GRN-M",   "size": "M",  "color": "Granatowy"},
            {"sku": "DRS-GRN-L",   "size": "L",  "color": "Granatowy"},
            {"sku": "DRS-GRN-XL",  "size": "XL", "color": "Granatowy"},
        ],
    },
    {
        "name": "Szorty Sportowe",
        "slug": "szorty-sportowe",
        "description": "Lekkie i przewiewne szorty sportowe wykonane z szybkoschnącego materiału. W pasie elastyczna guma z regulacją sznurkiem. Idealne na trening, siłownię i ciepłe dni. Wbudowana siateczkowa bielizna zapewnia wygodę.",
        "price": 79.99,
        "compare_price": 99.99,
        "category": "Spodnie",
        "brand": "Mercha",
        "variants": [
            {"sku": "SZT-CZR-S",   "size": "S",  "color": "Czarny"},
            {"sku": "SZT-CZR-M",   "size": "M",  "color": "Czarny"},
            {"sku": "SZT-CZR-L",   "size": "L",  "color": "Czarny"},
            {"sku": "SZT-CZR-XL",  "size": "XL", "color": "Czarny"},
            {"sku": "SZT-NIE-M",   "size": "M",  "color": "Niebieski"},
            {"sku": "SZT-NIE-L",   "size": "L",  "color": "Niebieski"},
            {"sku": "SZT-CZW-M",   "size": "M",  "color": "Czerwony"},
            {"sku": "SZT-CZW-L",   "size": "L",  "color": "Czerwony"},
        ],
    },

    # ── Buty ──
    {
        "name": "Sneakersy White Leather",
        "slug": "sneakersy-white-leather",
        "description": "Ponadczasowe białe sneakersy ze skóry ekologicznej. Minimalistyczny design pasujący do wszystkiego – od jeansów po garnitur. Miękka wyściółka i wyprofilowana wkładka zapewniają komfort przez cały dzień.",
        "price": 299.99,
        "compare_price": 359.99,
        "category": "Buty",
        "brand": "Mercha",
        "variants": [
            {"sku": "SNK-BIA-39", "size": "39", "color": "Biały"},
            {"sku": "SNK-BIA-40", "size": "40", "color": "Biały"},
            {"sku": "SNK-BIA-41", "size": "41", "color": "Biały"},
            {"sku": "SNK-BIA-42", "size": "42", "color": "Biały"},
            {"sku": "SNK-BIA-43", "size": "43", "color": "Biały"},
            {"sku": "SNK-BIA-44", "size": "44", "color": "Biały"},
        ],
    },
    {
        "name": "Buty Do Biegania Pro",
        "slug": "buty-do-biegania-pro",
        "description": "Profesjonalne buty do biegania z zaawansowaną amortyzacją i systemem stabilizacji stopy. Cholewka z oddychającej siateczki, podeszwa z gumy o wysokiej przyczepności. Zaprojektowane dla biegaczy szukających maksymalnego komfortu.",
        "price": 399.99,
        "compare_price": 479.99,
        "category": "Buty",
        "brand": "Mercha",
        "variants": [
            {"sku": "BIE-CZR-40", "size": "40", "color": "Czarny"},
            {"sku": "BIE-CZR-42", "size": "42", "color": "Czarny"},
            {"sku": "BIE-CZR-44", "size": "44", "color": "Czarny"},
            {"sku": "BIE-CZR-46", "size": "46", "color": "Czarny"},
            {"sku": "BIE-NIE-40", "size": "40", "color": "Niebieski"},
            {"sku": "BIE-NIE-42", "size": "42", "color": "Niebieski"},
            {"sku": "BIE-NIE-44", "size": "44", "color": "Niebieski"},
            {"sku": "BIE-CZW-42", "size": "42", "color": "Czerwony"},
            {"sku": "BIE-CZW-44", "size": "44", "color": "Czerwony"},
        ],
    },
    {
        "name": "Trampki Vintage Canvas",
        "slug": "trampki-vintage-canvas",
        "description": "Klasyczne trampki z płócienną cholewką w stylu vintage. Gumowa podeszwa z charakterystycznym bieżnikiem. Lekkie, wygodne i niezwykle stylowe. Must-have w każdej kolekcji obuwia.",
        "price": 179.99,
        "compare_price": None,
        "category": "Buty",
        "brand": "Mercha",
        "variants": [
            {"sku": "TRM-BIA-39", "size": "39", "color": "Biały"},
            {"sku": "TRM-BIA-40", "size": "40", "color": "Biały"},
            {"sku": "TRM-BIA-41", "size": "41", "color": "Biały"},
            {"sku": "TRM-BIA-42", "size": "42", "color": "Biały"},
            {"sku": "TRM-BIA-43", "size": "43", "color": "Biały"},
            {"sku": "TRM-CZR-40", "size": "40", "color": "Czarny"},
            {"sku": "TRM-CZR-41", "size": "41", "color": "Czarny"},
            {"sku": "TRM-CZR-42", "size": "42", "color": "Czarny"},
            {"sku": "TRM-CZR-43", "size": "43", "color": "Czarny"},
        ],
    },

    # ── Akcesoria ──
    {
        "name": "Czapka Beanie Merino",
        "slug": "czapka-beanie-merino",
        "description": "Ciepła czapka zimowa wykonana z najwyższej jakości wełny merino. Miękka, nie swędzi i doskonale izoluje ciepło. Uniwersalny fason pasujący do każdej stylizacji – od miejskiej po górską.",
        "price": 49.99,
        "compare_price": 69.99,
        "category": "Akcesoria",
        "brand": "Mercha",
        "variants": [
            {"sku": "CAP-CZR-OS", "size": "One Size", "color": "Czarny"},
            {"sku": "CAP-SZR-OS", "size": "One Size", "color": "Szary"},
            {"sku": "CAP-BRD-OS", "size": "One Size", "color": "Bordowy"},
            {"sku": "CAP-GRN-OS", "size": "One Size", "color": "Granatowy"},
        ],
    },
    {
        "name": "Plecak Miejski 30L",
        "slug": "plecak-miejski-30l",
        "description": "Pojemny plecak miejski o pojemności 30 litrów. Wyposażony w kieszeń na laptopa do 15.6\", liczne przegrody organizujące i boczną kieszeń na butelkę. Wodoodporny materiał i wzmocnione szwy zapewniają trwałość na lata.",
        "price": 159.99,
        "compare_price": 199.99,
        "category": "Akcesoria",
        "brand": "Mercha",
        "variants": [
            {"sku": "PLK-CZR-OS", "size": "One Size", "color": "Czarny"},
            {"sku": "PLK-GRN-OS", "size": "One Size", "color": "Granatowy"},
            {"sku": "PLK-SZR-OS", "size": "One Size", "color": "Szary"},
        ],
    },
    {
        "name": "Skarpety Sportowe 3-Pack",
        "slug": "skarpety-sportowe-3-pack",
        "description": "Zestaw 3 par skarpet sportowych wykonanych z bawełny z domieszką elastanu. Wzmocnione pięty i palce, wentylacyjne pasy na stopie. Idealne na trening i codzienne użytkowanie. Każdy pack zawiera trzy różne kolory.",
        "price": 29.99,
        "compare_price": 39.99,
        "category": "Akcesoria",
        "brand": "Mercha",
        "variants": [
            {"sku": "SKR-S-BIA", "size": "S", "color": "Biały"},
            {"sku": "SKR-M-BIA", "size": "M", "color": "Biały"},
            {"sku": "SKR-L-BIA", "size": "L", "color": "Biały"},
            {"sku": "SKR-S-CZR", "size": "S", "color": "Czarny"},
            {"sku": "SKR-M-CZR", "size": "M", "color": "Czarny"},
            {"sku": "SKR-L-CZR", "size": "L", "color": "Czarny"},
            {"sku": "SKR-M-SZR", "size": "M", "color": "Szary"},
            {"sku": "SKR-L-SZR", "size": "L", "color": "Szary"},
        ],
    },
]

# ── Warehouse locations ─────────────────────────────────────────────────
WAREHOUSE_LOCATIONS = [
    {"code": "A1", "zone": "A", "aisle": "1", "rack": "1", "shelf": "1", "description": "Regał A, sektor północny"},
    {"code": "A2", "zone": "A", "aisle": "1", "rack": "1", "shelf": "2", "description": "Regał A, sektor południowy"},
    {"code": "B1", "zone": "B", "aisle": "2", "rack": "1", "shelf": "1", "description": "Regał B, sektor wschodni"},
    {"code": "B2", "zone": "B", "aisle": "2", "rack": "1", "shelf": "2", "description": "Regał B, sektor zachodni"},
    {"code": "C1", "zone": "C", "aisle": "3", "rack": "1", "shelf": "1", "description": "Regał C, strefa wysyłkowa"},
]


async def seed(db: AsyncSession) -> None:
    """Insert sample data if the products table is empty."""

    existing = await db.scalar(select(Product).limit(1))
    if existing:
        logger.info("Products already exist, skipping seed.")
        print("✓ Produkty już istnieją w bazie, pomijam seed.")
        return

    # ── Categories ──────────────────────────────────────────────────────
    categories = [Category(**c) for c in CATEGORIES]
    db.add_all(categories)
    await db.flush()
    cat_map = {c.name: c.id for c in categories}
    logger.info("Added %d categories.", len(categories))

    # ── Products & variants ─────────────────────────────────────────────
    products = []
    all_variants = []
    variants_by_product = []
    for p_data in PRODUCTS:
        cat_id = cat_map[p_data.pop("category")]
        variants_data = p_data.pop("variants")
        product = Product(**p_data, category_id=cat_id)
        products.append(product)
        variants_by_product.append(variants_data)
        db.add(product)

    await db.flush()

    for product, v_data_list in zip(products, variants_by_product):
        for v_data in v_data_list:
            variant = ProductVariant(**v_data, product_id=product.id)
            all_variants.append(variant)
            db.add(variant)

    await db.flush()
    logger.info("Added %d products with %d variants.", len(products), len(all_variants))

    # ── Warehouse locations ─────────────────────────────────────────────
    locations = [WarehouseLocation(**loc) for loc in WAREHOUSE_LOCATIONS]
    db.add_all(locations)
    await db.flush()
    logger.info("Added %d warehouse locations.", len(locations))

    # ── Initial stock ───────────────────────────────────────────────────
    inventory_count = 0
    for variant in all_variants:
        # Pick 1-2 random locations per variant
        variant_locations = random.sample(locations, k=random.randint(1, 2))
        for loc in variant_locations:
            quantity = random.randint(10, 50)
            db.add(Inventory(
                variant_id=variant.id,
                location_id=loc.id,
                quantity=quantity,
                low_stock_threshold=5,
            ))
            inventory_count += 1

    await db.commit()
    print(f"✓ Dodano {len(categories)} kategorii, {len(products)} produktów, "
          f"{len(all_variants)} wariantów, {len(locations)} lokalizacji "
          f"magazynowych i {inventory_count} stanów magazynowych.")


async def main():
    logging.basicConfig(level=logging.INFO)
    async with async_session_factory() as session:
        await seed(session)


if __name__ == "__main__":
    asyncio.run(main())
