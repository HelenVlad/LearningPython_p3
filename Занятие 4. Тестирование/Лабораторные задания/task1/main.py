from random import choice, randint


class Mammals:
    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализация экземпляра класса Mammals.

        Args:
            gender (str): Пол животного.
            weight (int, float): Вес животного.
        """
        self.__settings = kwargs
        self._weight = self.check(min_num=self.__settings['min_num'],
                                  max_num=self.__settings['max_num'],
                                  units=self.__settings['units'],
                                  value=self.__settings['value'])
        self.__gender = self.check_str(["м", "ж"], value=self.__settings['gender'])

    @staticmethod
    def check(min_num: (int, float), max_num: (int, float), units: str, value):
        """
        Метод, проверяющий значения на соответствие указанным критериям.

        Args:
        - min_num: int или float, минимальное допустимое значение
        - max_num: int или float, максимальное допустимое значение
        - units: str, единицы измерения значения
        - value: значение для проверки

        Returns:
        - проверенное значение value

        Raises:
        - ValueError, если переданное значение не попадает в указанный диапазон или не является числом.

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
        Метод для проверки значения аргумента функции.

        Проверяет, что значение аргумента функции находится в заданном списке.

        Args:
            lst (list): Список допустимых значений для проверки.
            value (str): Список допустимых значений для проверки.

        Returns:
            value (str): Соответствующее критерием значение

        Raises:
            ValueError: Если значение последнего аргумента функции не находится в заданном списке.

        """

        if value not in lst:
            raise ValueError(
                f"Для установления атрибута используются обозначения из списка: {lst}. Введенное значение - {value}")
        else:
            return value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = self.check(min_num=self.__settings['min_num'],
                                  max_num=self.__settings['max_num'],
                                  units=self.__settings['units'],
                                  value=value)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        raise AttributeError("Данный атрибут изменить нельзя")

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, value):
        raise AttributeError("Данный атрибут изменить нельзя")

    def eats(self):
        """
        Метод, описывающий питание животного.
        """
        pass

    @classmethod
    def reproduces_offspring(cls, object1, object2):
        """
        Метод, описывающий размножение животного.
        """
        if not type(object1) == type(object2) or object1.gender == object2.gender:
            raise TypeError(f'Происходит что-то не то')
        else:
            child = cls(*object1.data_child()[-1])
            return child

    @staticmethod
    def data_child():
        return __class__.__name__, [1, 50, 'кг', randint(1, 50), choice(["м", "ж"])]

    def movement(self):
        """
        Метод, описывающий движение животного.
        """
        pass


class Lions(Mammals):
    def __init__(self, gender: str, weight: (int, float)) -> None:
        """
        Инициализация экземпляра класса Lions.

        Args:
            gender (str): Пол льва.
            weight (int, float): Вес льва.
        """
        super().__init__(min_num=1, max_num=300, units='кг', value=weight, gender=gender)
        self.predator = True
        if gender == 'м':
            self.mane = True
        else:
            self.mane = False

    def __repr__(self):
        return f'{__class__.__name__}(gender={self.gender}, weight={self.weight})'
    def data_child(self):
        return __class__.__name__, [choice(["м", "ж"]), randint(1, 5)]

    def hunting(self):
        """
        Метод, описывающий добычу пропитания.
        """
        pass


class Giraffe(Mammals):
    """
    Класс, представляющий жирафа.

    """

    def __init__(self, gender: str, weight: (int, float), neck_length: (int, float), spots: int) -> None:
        """
        Инициализация экземпляра класса Giraffe.

        Args:
            gender (str): Пол жирафа.
            weight (int, float): Вес жирафа.
            neck_length (int, float): Длина шеи жирафа.
            spots (int): Количество пятен на теле жирафа.
        """
        super().__init__(min_num=35, max_num=1900, units='кг', value=weight, gender=gender)
        self.neck_length = self.check(min_num=60, max_num=3000, units='см', value=neck_length)
        self.spots = self.check(min_num=0, max_num=500, units='ед', value=spots)
        self.predator = False

    def __repr__(self):
        return f'{__class__.__name__}' \
               f'(gender={self.gender}, ' \
               f'weight={self.weight}, ' \
               f'neck_length={self.neck_length}, ' \
               f'spots={self.spots})'

    @staticmethod
    def data_child():
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
    animal2 = Mammals(min_num=1, max_num=300, units='кг', value=150, gender="м")
