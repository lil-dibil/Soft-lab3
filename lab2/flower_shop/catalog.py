# catalog.py
# Работа с каталогом товаров для системы "Цветочный магазин"

def show_catalog(db):
    """Выводит список товаров из базы данных."""
    products = db.get_products()

    print("\n=== КАТАЛОГ ТОВАРОВ ===")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} — {product['price']} руб. (в наличии: {product['stock']})")
