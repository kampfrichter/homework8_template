import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data():
    number_file = int(input("Выберите исходный фаил, нажмите 1 или 2\n"))
    if 0 < number_file < 3:
        source = f'Text_{number_file}.txt'
        print(read_all(source))
        if number_file == 1:
            dest = 'Text_2.txt'
        else:
            dest = 'Text_1.txt'

        number_row = int(input(f"введите номер копируемой строки \n"))

        with open(source, 'r') as input_f, open(dest, 'a') as output_f:
            lines = input_f.readlines()
            if number_row > 0 and number_row <= len(lines):
                output_f.write("\n" + lines[number_row - 1])
                print("Строка успешно скопирована.")
            else:
                print("Некорректный номер строки.")
    else:
        print("в списке всего 2 файла, выберете 1 или 2")


INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "Text_1.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        transfer_data()

