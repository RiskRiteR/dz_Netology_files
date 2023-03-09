from pprint import pprint

import os

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


list_file_address = ['1.txt', '2.txt', '3.txt']
list_text_all_files = []
for _ in range(len(list_file_address)):
    full_path = os.path.join(os.getcwd(), 'a_group_of_files_to_merge', list_file_address[_])
    with open(full_path, 'r', encoding='utf-8') as file:
        list_text_all_files.append(file.readlines())
list_text_all_files.sort()
list_text_all_files.reverse()


with open('sorted_file.txt', 'w', encoding='utf-8') as file:
    for i, _ in enumerate(list_text_all_files):
        file.write(list_file_address[i])
        file.write('\n')
        file.write(str(len(list_text_all_files[i])))
        file.write('\n')
        file.writelines(_)
        file.write('\n')
