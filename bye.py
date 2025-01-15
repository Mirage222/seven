bread = True 
cheese = True 
egg = True
meat = True

if bread and cheese and egg and meat:
    recommendation = "Чизбургер"
elif bread and egg and meat:
    recommendation = "Гамбургер"
elif bread and cheese:
    recommendation = "Бутерброд"
elif bread and egg:
    recommendation = "Омлет"
elif bread and meat:
    recommendation = "Котлеты"
else:
    recommendation = "Недостаточно ингредиентов для приготовления блюда"

print(f"Рекомендация: {recommendation}")