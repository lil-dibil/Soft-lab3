# user.py
# Работа с пользователями в системе "Цветочный магазин"

def login_user():
    """Имитация входа пользователя."""
    print("\n=== ВХОД В СИСТЕМУ ===")
    name = input("Введите ваше имя: ").strip()

    if not name:
        name = "Гость"

    user = {"name": name, "role": "customer"}
    print(f"Добро пожаловать, {name}!\n")
    return user
