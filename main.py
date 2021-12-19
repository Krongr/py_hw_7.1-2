def get_shopping_list_by_dishes(dishes: list, persons: int, cook_book: dict) -> dict:
    """Вычисляет необходимое количество ингредиентов для приготовления блюд 'dishes' из словаря с рецептами 'cook_book' на требуемое количество персон 'persons'.
    Возвращает словарь с необходимыми ингредиентами и их количеством.
    """
    pass

def wright_shopping_list_to_file(file_name='shopping_list.txt') -> None:
    """Записывает словарь (получаемый от функции 'get_shopping_list_by_dishes') в текстовый файл 'file_name'.
    """

def read_recipes_from_file(file_name='recipes.txt') -> list:
    """Считывает данные из текстового файла с рецептами 'file_name'.
    Возвращает список, каждый элемент которого содержит список строк, относящихся к одному рецепту. 
    """
    pass

def creat_cook_book(recipes_list: list, spliter=' | ') -> dict:
    """Возвращает словарь с рецептами, созданный на основе списка рецептов 'recipes_list'.
    """
    pass