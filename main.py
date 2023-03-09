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


def get_shop_list_by_dishes(dishes, person_count):
    dict_all_ingredients = {}
    for _ in [required_dict for _ in range(len(dishes)) for required_dict in cook_book[dishes[_]]]:
        if _['ingredient_name'] not in dict_all_ingredients:
            dict_all_ingredients.setdefault(_['ingredient_name'], {
                'measure': _['measure'], 'quantity': int(_['quantity']) * person_count
            })
        else:
            dict_all_ingredients[_['ingredient_name']]['quantity'] += int(_['quantity']) * person_count
    return pprint(dict_all_ingredients)
