def get_shopping_list_by_dishes(dishes: list, persons: int, cook_book: dict) -> dict:
    """Вычисляет необходимое количество ингредиентов для приготовления блюд 'dishes' из словаря с рецептами 'cook_book' на требуемое количество персон 'persons'.
    Возвращает словарь с необходимыми ингредиентами и их количеством.
    """
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_list:
                    shopping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (ingredient['quantity'] * persons)}
                else:
                    shopping_list[ingredient['ingredient_name']]['quantity'] += (ingredient['quantity'] * persons)
    return shopping_list


def creat_cook_book(file_name='recipes.txt', separator_for_file='', separator=' | ') -> dict:
    """Возвращает словарь с рецептами, созданный на основе списка, полученного от функции 'read_recipes_from_file('file_name')' ."""
    cook_book = {}
    for dish_list in read_recipes_from_file(file_name, separator_for_file):
        cook_book[dish_list[0]] = []
        for i in range(1, len(dish_list)):
            dish_list[i] = dish_list[i].split(separator)
            dish_list[i] = {'ingredient_name': dish_list[i][0], 'quantity': int(dish_list[i][1]), 'measure': dish_list[i][2]}
            cook_book[dish_list[0]].append(dish_list[i])
    return cook_book


def wright_shopping_list_to_file(dishes: list, persons: int, cook_book: dict, file_name='shopping_list.txt') -> None:
    """Записывает словарь, полученный от функции 'get_shopping_list_by_dishes', в текстовый файл 'file_name'."""
    shopping_list = get_shopping_list_by_dishes(dishes, persons, cook_book)
    with open(file_name, 'wt', encoding='utf-8') as file:
        for ingredient in shopping_list:
            file.write(f"{ingredient} - {shopping_list[ingredient]['quantity']} {shopping_list[ingredient]['measure']}\n")


def read_recipes_from_file(file_name='recipes.txt', separator='') -> list:
    """Считывает данные из текстового файла с рецептами 'file_name'.
    Возвращает список, каждый элемент которого содержит список строк, относящихся к одному рецепту. Рецепты разделяются по строке-разделителю 'separator'.
    """
    recipes_list = []
    dish_list = []
    with open(file_name, 'rt', encoding='utf-8') as file:
        for line in file:
            if line.strip() != separator and line.strip() != ' ':
                if not line.strip().isdigit():
                    dish_list.append(line.strip())
            else:
                if dish_list:
                    recipes_list.append(dish_list)
                dish_list = []
        if dish_list:
            recipes_list.append(dish_list)
    return recipes_list


list_of_dishes = ['Омлет', 'Утка по-пекински', 'Фахитос']

print(creat_cook_book())
print(get_shopping_list_by_dishes(list_of_dishes, 6, creat_cook_book()))
wright_shopping_list_to_file(list_of_dishes, 6, creat_cook_book())