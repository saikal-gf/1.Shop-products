
products = {
    "Хлеб": 25,
    "Молоко": 50,
    "Яйца (10 шт)": 60,
    "Картошка (1 кг)": 30,
    "Сахар (1 кг)": 55,
    "Мука (2 кг)": 90
}

cart = {}
total = 0

print("👩‍💼 Продавец: Добро пожаловать в наш продуктовый магазин!")
print("Вот список товаров и их цены:")

for product, price in products.items():
    print(f"- {product} — {price} сом")

while True:
    action = input("\nЧто хотите сделать? (цена / купить / корзина / итог / выход): ").lower()

    if action == "цена":
        name = input("👤 Клиент: Сколько стоит... ").capitalize()
        if name in products:
            print(f"👩‍💼 Продавец: {name} стоит {products[name]} сом.")
        else:
            print("👩‍💼 Продавец: Такого товара нет.")

    elif action == "купить":
        name = input("👤 Клиент: Хочу купить... ").capitalize()
        if name in products:
            qty = input("Сколько штук/кг?: ")
            if qty.isdigit():
                qty = int(qty)
                cart[name] = cart.get(name, 0) + qty
                total += products[name] * qty
                print(f"✅ Добавлено в корзину: {name} x{qty}")
            else:
                print("❌ Нужно ввести количество числом!")
        else:
            print("❌ Такого товара нет.")

    elif action == "корзина":
        print("\n🛒 Ваша корзина:")
        if not cart:
            print("Корзина пуста.")
        else:
            for item, qty in cart.items():
                print(f"- {item} x{qty} = {products[item] * qty} сом")
            print(f"💰 Промежуточный итог: {total} сом")

    elif action == "итог":
        discount = 0
        if total >= 500:
            discount = int(total * 0.1) 
            print(f"🎉 Вам положена скидка 10%: -{discount} сом")

        final = total - discount
        print(f"\n✅ Общая сумма к оплате: {final} сом")
        print("🙏 Спасибо за покупку!")
        break

    elif action == "выход":
        print("👩‍💼 Продавец: Хорошо! Будем рады видеть вас снова!")
        break

    else:
        print("🤔 Я не поняла. Напишите: цена / купить / корзина / итог / выход.")
