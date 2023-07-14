import re


class DataStorage:
    """
    Класс, отвечающий за хранение вычислений.
    """
    pass


class Display:
    """
    Класс, отвечающий за отображение данных.
    """
    pass


class InputPanel:
    """
    Класс, отвечающий за ввод данных пользователем.
    """
    # паттерн для инструментов класса BaseCalculator
    pattern_BC = re.compile(r'^(\d+(?:\.\d+)?)\s*([-+*/])\s*(\d+(?:\.\d+)?)')
    # паттерн для инструментов класса AccountingCalculator
    pattern_AC = re.compile(r'^(\d+(?:\.\d+)?)\s*([-+*/])\s*(\d+(?:\.\d+)?)$|^([AC][CE][C][MS][MC][MR][M-][M+])$')

    def __init__(self, exp):
        self.expression = self.detection(self.pattern_BC, ''.join(exp.split(' ')))


    def detection(self, pat, string):
        match = re.match(pat, string)
        if match:
            first_number = match.group(1)
            operator = match.group(2)
            second_number = match.group(3)
        return [float(first_number), operator, float(second_number)]


class Application:
    def start(self):
        print('Введите выражение')


class BaseCalculator:
    """
    Класс базового калькулятора. Имеет базовые функции:
    - Сложение;
    - Вычитание;
    - Умножение;
    - Деление;
    - Смена знака;
    - Вычисление квадратного корня;
    - Возведение в степень;
    - Расчет процентов.
    """

    def __init__(self, lst):
        self.string = lst
        self.calc = self.calculation(self.string)

    def calculation(self, strin):
        """
        Метод, который определяет тип операции и производит вычисление.
        """
        var = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        if strin:

            result = var[strin[1]](strin[0], strin[2])

        return result


    def addition(self, a, b):
        """
        Метод, который выполняет складывание.
        """
        pass

    def subtraction(self):
        """
        Метод, который выполняет вычитание.
        """
        pass

    def division(self):
        """
        Метод, который выполняет деление.
        """
        pass

    def multiplication(self):
        """
        Метод, который выполняет умножение.
        """
        pass

    def sign_change(self):
        """
        Метод, который выполняет смену знака.
        """
        pass

    def square_root(self):
        """
        Метод, который выполняет вычисление квадратного корня.
        """
        pass

    def exponentiation(self):
        """
        Метод, который выполняет возведение в степень.
        """
        pass

    def percent(self):
        """
        Метод, который выполняет вычисление процента.
        """
        pass


class AccountingCalculator(BaseCalculator):
    """
    Класс бухгалтерского калькулятора. Имеет функции помимо базовых:
    - Добавление двух нулей к введенному числу
    - Ведение истории вычислений
    - АС - удаление всех введенных данных, в т.ч. из памяти
    - СЕ - очищение только текущего поля, не затрагивает данные в памяти
    - С - очистка ввода
    - MS - запись текущего значения на дисплее в буфер памяти
    - MC - удаление данных в памяти
    - MR - отображение содержимого буфера
    - M- - вычитание значения в буфере из текущего значения на дисплее
    - M+ - сложение значения в буфере из текущего значения на дисплее

    """

    def history_of_calculation(self):
        pass


class EngineerCalculator(AccountingCalculator):
    """
    Класс инженерного калькулятора. Имеет функции помимо базовых:
    - Вычисление:
        -- Sin
        -- Cos
        -- Tg
        -- Ctg
        -- Asin
        -- Acos
        -- Atg
        -- Actg
    - Вычисление логарифма по основанию
    - Возведение 10 в n-ю степень
    - Просмотр число Пи и число Эйлера
    - Деление целого на текущее, т.е. ф-я позволяет узнать,
    сколько текущий показатель составляет от единого целого (1/x).

    """

    def __init__(self):
        pass


if __name__ == "__main__":
    lst = InputPanel('       10   +   35     ')
    print(lst.expression)

    calc = BaseCalculator(lst.expression)

    print(calc.calc)