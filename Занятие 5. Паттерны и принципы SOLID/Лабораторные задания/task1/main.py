import re


class DataStorage:
    """
    Класс, отвечающий за хранение вычислений.
    """

    def __init__(self):
        self.storage = []

    def add(self, value):
        self.storage.append(value)

    def clear_storage(self):
        self.storage.clear()

    def memory_operation(self):
        return self.storage[-1]

    def view(self):
        return self.storage


class UserInterface:
    """
    Класс, отвечающий за ввод данных пользователем и отображение результата.
    """

    def __init__(self, exp, pat):
        self.pattern = pat
        self.string = ''.join(exp.split(' '))
        self.expression = self.detection(self.pattern, self.string)

    @staticmethod
    def detection(pat, string):
        matches = re.findall(pat, string)
        if not matches:
            raise ValueError('Не найдено совпадений.')

        for match in matches:
            # Проверка, содержит ли какая-либо группа непустое значение
            if any(val.strip() for val in match):
                res = [val.strip() for val in match if val.strip()]
                return res

    def data_output(self, data):
        print('+' + '-' * 20 + '+')
        print(f'Введенное выражение:\n{self.string}')
        print('+' + '-' * 20 + '+')
        print(f'Результат вычисления:\n{data}')
        print('+' + '-' * 20 + '+')


class ApplicationBC:
    # паттерн для инструментов класса BaseCalculator
    pattern = re.compile(r'^(\d+(?:\.\d+)?)\s*([-+*/%])\s*(\d+(?:\.\d+)?)')

    def __init__(self):
        self.app = self.action()

    def calc(self, lst):
        calculation = BaseCalculator(lst)
        return calculation

    def data(self):
        entry = UserInterface(input('Введите выражение:\n->'), self.pattern)
        calculation = self.calc(entry.expression)
        entry.data_output(calculation.calc)
        return calculation

    @staticmethod
    def hello():
        return 'Приветствуем в приложении "Калькулятор"! Набор функций:\n \
                - Сложение;\n \
                - Вычитание;\n \
                - Умножение;\n \
                - Деление;\n \
                - Расчет процентов.\n \
Приложение поддерживает ввод типа а(+-*/%)b \n \
    Пример:\n \
    150+450 \n \
    150-100 \n \
    150*5 \n \
    150/2 \n \
    150%2\n'

    def action(self):
        print(self.hello())
        while True:
            self.data()


storage_OBJ = DataStorage()  # КОНСТАНТА


class ApplicationAC(ApplicationBC):
    pattern = re.compile(
        r'(?:(\d+\.\d+|\d+)(?:\s*([-+*/%])\s*([0-9]+|M)|\s*([MC])|(?<=\d)\s*([-+*/%])\s*M(?=/0)))|(MC)|(MR)')

    def calc(self, lst):
        calculation = AccountingCalculator(lst)
        return calculation

    @staticmethod
    def hello2():
        return 'Новые функции:\n \
                - Ведение истории вычислений \n \
                - MC - удаление данных в памяти \n \
                - MR - отображение содержимого буфера \n \
                - M- - вычитание последнего значения в буфере c новым значением \n \
                - M+ - сложение последнего значения в буфере c новым значением \n \
    Пример ввода: \n \
    150+M \n \
    150-M \n \
    MR \n \
    MC'

    def action(self):
        print(self.hello())
        print(self.hello2())
        while True:
            calculation = self.data()
            if calculation.string not in [['MC'], ['MR']]:
                storage_OBJ.add(calculation)


class BaseCalculator:
    """
    Класс базового калькулятора. Имеет базовые функции:
    - Сложение;
    - Вычитание;
    - Умножение;
    - Деление;
    - Расчет процентов.
    """

    def __init__(self, lst):
        self.string = lst
        self.calc = self.base_calculation(self.string)

    def __str__(self):
        return f"{self.calc}"

    def __repr__(self):
        return f"{''.join(self.string)}={self.calc}"

    @staticmethod
    def base_calculation(strin):
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
    - Ведение истории вычислений
    - MC - удаление данных в памяти
    - MR - отображение содержимого буфера
    - M- - вычитание последнего значения в буфере c новым значением
    - M+ - сложение последнего значения в буфере c новым значением

    """

    def __init__(self, lst):
        self.string = lst
        self.calc = None
        self.function_selection(self.string)

    def function_selection(self, value):
        signs = ['-', '+', '*', '/', '%']

        if any([x == 'M' for x in value]):
            val_indx = value.index('M')
            val = storage_OBJ.memory_operation()
            value[val_indx] = str(val.calc)
            self.calc = self.base_calculation(value)

        elif any([x in signs for x in value]):
            self.calc = self.base_calculation(value)

        elif value == ['MC']:
            storage_OBJ.clear_storage()
            self.calc = 'История очищена'

        elif value == ['MR']:
            self.calc = storage_OBJ.view()

        else:
            raise TypeError('Функция не опознана или не существует')


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
    app = ApplicationAC()
