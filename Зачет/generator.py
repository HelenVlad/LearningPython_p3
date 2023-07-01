from random import randint
from itertools import islice


def data_generator() -> str:
    '''
    Функция data_generator() возвращает случайную строку из файла "text.txt".
    Сначала функция генерирует случайное число от 1 до 100, которое используется для выбора строки из файла.
    Функция открывает файл с помощью with open(filename), затем использует itertools.islice
    для выбора соответствующей строки и next() для выбора следующей строки.
    :return: Возвращает строку без символа перевода строки.
    '''
    filename = "text.txt"
    while True:
        line_num = randint(1, 100)
        with open(filename, encoding='utf-8') as file:
            lines = islice(file, line_num - 1, line_num)
            line = next(lines)
        yield eval(line.replace('\n', ''))
