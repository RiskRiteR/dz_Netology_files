from pprint import pprint

with open('cook_book.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        food_name = i.strip()
        quantity_ingredients = int(file.readline())
        list_ingredients = []
        for j in range(quantity_ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            list_ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[food_name] = list_ingredients
pprint(cook_book, sort_dicts=False)

