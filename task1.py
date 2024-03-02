"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
"""


def file_info(str_input: str) -> tuple:
    *path_lst, name = str_input.split('/')
    name, extension = (i for i in name.split("."))
    path = '/'.join(path_lst[0:-1])
    return path, name, extension


if __name__ == "__main__":
    str_path = 'C:/Users/adisc/PycharmProjects/PYseminar5/task1.py'
    print(file_info(str_path))
