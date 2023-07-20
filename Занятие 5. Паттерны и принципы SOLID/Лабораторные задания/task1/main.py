import re


class DataStorage:
    """
    Класс, отвечающий за хранение вычислений.
    """

    def __init__(self):
        self.storage = []

    def add(self, value):
        self.storage.append(value)


class UserInterface:
    """
    Класс, отвечающий за ввод данных пользователем и отображение результата.
    """
    # паттерн для инструментов класса BaseCalculator
    pattern_BC = re.compile(r'^(\d+(?:\.\d+)?)\s*([-+*/%])\s*(\d+(?:\.\d+)?)')
    # паттерн для инструментов класса AccountingCalculator
    pattern_AC = re.compile(r'^(\d+(?:\.\d+)?)\s*([-+*/%])\s*(\d+(?:\.\d+)?)$|^([AC][CE][C][MS][MC][MR][M-][M+])$')

    def __init__(self, exp):
        self.string = ''.join(exp.split(' '))
        self.expression = self.detection(self.pattern_BC, self.string)

    # def detection(self, pat, string):
    #     match = re.match(pat, string)
    #     try:
    #         if match:
    #             first_number = match.group(1)
    #             operator = match.group(2)
    #             second_number = match.group(3)
    #         print(f'{match.group(10)=}')
    #         return [float(first_number), operator, float(second_number)]
    #     except UnboundLocalError:
    #         raise ValueError('Введено неизвестное значение.')

    def detection(self, pat, string):
        match = re.match(pat, string)
        try:
            result = []
            num = 1
            while True:
                try:
                    result.append(match.group(num))
                    num += 1
                except IndexError:
                    break
            return result
        except UnboundLocalError:
            raise ValueError('Введено неизвестное значение.')

    def data_output(self, data):
        print('+' + ('-') * 20 + '+')
        print(f'Введенное выражение:\n{self.string}')
        print('+' + ('-') * 20 + '+')
        print(f'Результат вычисления:\n{data}')
        print('+' + ('-') * 20 + '+')


class Application_BC:
    def __init__(self):
        self.app = self.action()

    def calc(self, lst):
        calculation = BaseCalculator(lst)
        return calculation

    def data(self):
        entry = UserInterface(input('Введите выражение:\n->'))
        calculation = self.calc(entry.expression)
        entry.data_output(calculation.calc)
        return calculation

    def action(self):
        while True:
            self.data()


class Application_AC(Application_BC):

    def calc(self, lst):
        calculation = AccountingCalculator(lst)
        return calculation

    def action(self):
        storage = DataStorage()
        while True:
            calculation = self.data()
            storage.add(calculation)
            print(storage.storage)


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
        self.calc = self.base_calculation(self.string)

    def __str__(self):
        return f"{self.calc}"

    def __repr__(self):
        return f"{''.join(self.string)}={self.calc}"

    def base_calculation(self, strin):
        """
        Метод, который определяет тип операции и производит вычисление.
        """
        var = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: (a * b) / 100
        }
        if len(strin) >= 3:
            result = var[strin[1]](float(strin[0]), float(strin[2]))
        else:
            raise TypeError('На данный момент поддерживаются действия только  между двумя числами')

        return result


class AccountingCalculator(BaseCalculator):
    """
    Класс бухгалтерского калькулятора. Имеет функции помимо базовых:
    - Добавление двух нулей к введенному числу
    - Ведение истории вычислений
    - АС - удаление всех введенных данных, в т.ч. из памяти
    - СЕ - очищение только текущего поля, не затрагивает данные в памяти
    # - С - очистка ввода
    - MS - запись текущего значения на дисплее в буфер памяти
    - MC - удаление данных в памяти
    - MR - отображение содержимого буфера
    - M- - вычитание значения в буфере из текущего значения на дисплее
    - M+ - сложение значения в буфере из текущего значения на дисплее

    """

    def __init__(self, lst):
        self.string = lst
        self.calc = None
        self.function_selection(self.string)

    def function_selection(self, value):
        signs = ['-', '+', '*', '/', '%']
        signs2 = ['AC', 'CE', 'C', 'MC', 'MS', 'MR', 'M+', 'M-']

        if value[1] in signs:
            self.calc = self.base_calculation(value)
        elif value[1] in signs2:
            self.calc = self.history_of_calculation(value)
        else:
            raise TypeError('Функция не опознана или не существует')

    def history_of_calculation(self, value):
        return f'Функция в разработке'


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
    app = Application_AC()