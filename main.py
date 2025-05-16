print("Добро пожаловать в GamerShop!")
print("Вот наш ассортимент:")

items = {
    "Мышка игровая": 1500,
    "Клавиатура механическая": 3000,
    "Монитор 144Hz": 12000
}

for item, price in items.items():
    print(f"{item} - {price} сом")

basket = []
total = 0

while True:
    choice = input("\nВведите название товара (или 'стоп' для завершения): ")
    if choice.lower() == "стоп":
        break
    elif choice in items:
        basket.append(choice)
        total += items[choice]
        print(f"{choice} добавлен в корзину. Текущая сумма: {total} сом")
    else:
        print("Такого товара нет в списке. Попробуйте снова.")

print("\nВаш чек:")
for item in basket:
    print(f"- {item} - {items[item]} сом")
print(f"Итоговая сумма: {total} сом")

print("\nСпасибо за покупку! Удачи в играх! 🎮")
