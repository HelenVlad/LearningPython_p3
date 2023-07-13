from random import choice, randint


class Mammals:
    def __init__(self, min_num, max_num, units, value, gender) -> None:
        """
        Конструктор класса Mammals.

        Параметры:
        - min_num (int, float): Минимальное допустимое значение для атрибута веса.
        - max_num (int, float): Максимальное допустимое значение для атрибута веса.
        - units (str): Единицы измерения для атрибута веса.
        - value (int, float): Значение атрибута веса.
        - gender (str): Пол животного ('м' - мужской, 'ж' - женский).
        """
        self._weight = self.check(min_num, max_num, units, value)
        self.__gender = self.check_str(["м", "ж"], value=gender)
        self.__data = [min_num, max_num, units]

    @staticmethod
    def check(min_num: (int, float), max_num: (int, float), units: str, value):
        """
        Проверяет, соответствует ли значение атрибута веса заданным допустимым значениям.

        Параметры:
        - min_num (int, float): Минимальное допустимое значение для атрибута веса.
        - max_num (int, float): Максимальное допустимое значение для атрибута веса.
        - units (str): Единицы измерения для атрибута веса.
        - value: Значение атрибута веса для проверки.

        Возвращает:
        - value: Значение атрибута веса, если оно соответствует допустимым значениям.

        Вызывает исключение ValueError, если значение атрибута веса не соответствует допустимым значениям.
        """
        if isinstance(value, (int, float)):
            if not max_num >= value >= min_num:
                raise ValueError(
                    f"Значение должно находиться в промежутке от {min_num}{units} до {max_num}{units}. \
Введенное значение - {value}")
            else:
                return value
        else:
            raise ValueError(f"Значение должно быть числом (типа int или float)")

    @staticmethod
    def check_str(lst: list, value):
        """
        Проверяет, соответствует ли значение атрибута пола заданным допустимым значениям.

        Параметры:
        - lst (list): Список допустимых значений для атрибута пола.
        - value: Значение атрибута пола для проверки.

        Возвращает:
        - value: Значение атрибута пола, если оно соответствует допустимым значениям.

        Вызывает исключение ValueError, если значение атрибута пола не соответствует допустимым значениям.
        """
        if value not in lst:
            raise ValueError(
                f"Для установления атрибута используются обозначения из списка: {lst}. Введенное значение - {value}")
        else:
            return value

    @property
    def weight(self):
        """
        Свойство, предоставляющее доступ к атрибуту веса.
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        """
        Сеттер для атрибута веса.

        Параметры:
        - value: Новое значение атрибута веса.

        Вызывает метод check для проверки нового значения атрибута веса.
        """
        self._weight = self.check(*self.__data, value)

    @property
    def gender(self):
        """
        Свойство, предоставляющее доступ к атрибуту пола.
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """
        Сеттер для атрибута пола.

        Параметры:
        - value: Новое значение атрибута пола.

        Вызывает исключение AttributeError, так как атрибут пола изменять нельзя.
        """
        raise AttributeError("Данный атрибут изменить нельзя")

    @property
    def data(self):
        """
        Свойство, предоставляющее доступ к атрибуту данных.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Сеттер для атрибута данных.

        Параметры:
        - value: Новое значение атрибута данных.

        Вызывает исключение AttributeError, так как атрибут данных изменять нельзя.
        """
        raise AttributeError("Данный атрибут изменить нельзя")

    def eats(self):
        return f'Животное {__class__.__name__} кушает'

    def movement(self):
        """
        Метод, описывающий движение животного.
        """
        return f'Животное {__class__.__name__} двигается'

    def __repr__(self):
        """
        Возвращает строковое представление объекта класса.
        """
        return f'{__class__.__name__}(gender={self.gender}, weight={self.weight})'

    @classmethod
    def reproduces_offspring(cls, object1, object2):
        """
        Статический метод, описывающий размножение потомков.

        Параметры:
        - object1: Первый объект для размножения.
        - object2: Второй объект для размножения.

        Возвращает:
        - child: Новый объект-потомок.

        Вызывает исключение TypeError, если объекты для размножения принадлежат разным классам или имеют одинаковый пол.
        """
        if not type(object1) == type(object2) or object1.gender == object2.gender:
            raise TypeError(f'Происходит что-то не то')
        else:
            child = cls(*object1.data_child()[-1])
            return child

    @staticmethod
    def data_child():
        """
        Статический метод, возвращающий данные для создания нового объекта-потомка.

        Возвращает:
        - class_name: Имя класса объекта-потомка.
        - params: Параметры для создания нового объекта-потомка.
        """
        return __class__.__name__, [1, 50, 'кг', randint(1, 50), choice(["м", "ж"])]




class Lions(Mammals):
    def __init__(self, gender: str, weight: (int, float)) -> None:
        """
        Конструктор класса Lions.

        Параметры:
        - gender (str): Пол льва ('м' - мужской, 'ж' - женский).
        - weight (int, float): Вес льва.
        """
        super().__init__(min_num=1, max_num=300, units='кг', value=weight, gender=gender)
        self.predator = True
        if gender == 'м':
            self.mane = True
        else:
            self.mane = False

    def __repr__(self):
        """
        Возвращает строковое представление объекта класса.
        """
        return f'{__class__.__name__}(gender={self.gender}, weight={self.weight})'

    def data_child(self):
        """
        Возвращает данные для создания нового объекта-потомка.

        Возвращает:
        - class_name: Имя класса объекта-потомка.
        - params: Параметры для создания нового объекта-потомка.
        """
        return __class__.__name__, [choice(["м", "ж"]), randint(1, 5)]

    def hunting(self):
        """
        Метод, описывающий добычу пропитания.
        """
        pass


class Giraffe(Mammals):
    def __init__(self, gender: str, weight: (int, float), neck_length: (int, float), spots: int) -> None:
        """
        Конструктор класса Giraffe.

        Параметры:
        - gender (str): Пол жирафа ('м' - мужской, 'ж' - женский).
        - weight (int, float): Вес жирафа.
        - neck_length (int, float): Длина шеи жирафа.
        - spots (int): Количество пятен на теле жирафа.
        """
        super().__init__(min_num=35, max_num=1900, units='кг', value=weight, gender=gender)
        self.neck_length = self.check(min_num=60, max_num=3000, units='см', value=neck_length)
        self.spots = self.check(min_num=0, max_num=500, units='ед', value=spots)
        self.predator = False

    def __repr__(self):
        """
        Возвращает строковое представление объекта класса.
        """
        return f'{__class__.__name__}' \
               f'(gender={self.gender}, ' \
               f'weight={self.weight}, ' \
               f'neck_length={self.neck_length}, ' \
               f'spots={self.spots})'

    @staticmethod
    def data_child():
        """
        Статический метод, возвращающий данные для создания нового объекта-потомка.

        Возвращает:
        - class_name: Имя класса объекта-потомка.
        - params: Параметры для создания нового объекта-потомка.
        """
        return __class__.__name__, [choice(["м", "ж"]), randint(35, 100), randint(60, 180), randint(0, 100)]

    def defense(self):
        """
        Метод, описывающий защиту от хищников.
        """
        pass


if __name__ == "__main__":
    tomas = Giraffe('м', 555.153, 2000.153, 456)
    glory = Giraffe('ж', 555.153, 2000.153, 456)
    miky = Giraffe.reproduces_offspring(tomas, glory)
    print(miky)

    endry = Lions('м', 300)
    marina = Lions('ж', 150)
    olfo = Lions.reproduces_offspring(endry, marina)
    print(olfo)

    animal = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")
    animal2 = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="ж")

    animal3 = Mammals.reproduces_offspring(animal, animal2)
    print(animal3)
