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


def sorts_files_by_text_length(file_list: list, locations):
    list_all_files = []
    dict_help = {}
    for _i, _j in enumerate(file_list):
        full_path = os.path.join(os.getcwd(), locations, _j)
        with open(full_path, 'r', encoding='utf-8') as files:
            list_all_files.append(files.readlines())
            dict_help.setdefault(len(list_all_files[_i]), _j)
    list_all_files.sort()
    list_all_files.reverse()

    with open('sorted_file.txt', 'w', encoding='utf-8') as files:
        for _i in list_all_files:
            files.write(dict_help[len(_i)])
            files.write('\n')
            files.write(str(len(_i)))
            files.write('\n')
            files.writelines(_i)
            files.write('\n')


sorts_files_by_text_length(['1.txt', '2.txt', '3.txt'], 'a_group_of_files_to_merge')
