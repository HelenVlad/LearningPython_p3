# TODO Написать 3 класса с документацией и аннотацией типов
def check(min_num: (int, float), max_num: (int, float), units: str):
    """
    Декоратор, проверяющий значения на соответствие указанным критериям.

    Args:
    - min_num: int или float, минимальное допустимое значение
    - max_num: int или float, максимальное допустимое значение
    - units: str, единицы измерения значения

    Returns:
    - функцию-обертку, которая проверяет переданные значения на соответствие критериям.

    Raises:
    - ValueError, если переданное значение не попадает в указанный диапазон или не является числом.

    Пример использования:
    @check(min_num=0, max_num=100, units='%')
    def check_percentage(value):
        return value

    При вызове функции check_percentage(75) будет возвращено 75, если значение находится в диапазоне от 0 до 100.
    В противном случае будет возбуждено исключение ValueError.
    """

    def decorate(func):
        def wrapper(*arg):
            if isinstance(arg[-1], (int, float)):

                if not max_num >= arg[-1] >= min_num:
                    raise ValueError(
                        f"Значение должно находиться в промежутке от {min_num}{units} до {max_num}{units}. \
Введенное значение - {arg[-1]}")
                else:
                    ret = list(func(arg[0], arg[-1]))
                    return ret[0]
            else:
                raise ValueError(f"Значение должно быть числом (типа int или float)")

        return wrapper

    return decorate

def check_str(lst: list):
    """
    Декоратор для проверки значения аргумента функции.

    Проверяет, что значение аргумента функции находится в заданном списке.

    Args:
        lst (list): Список допустимых значений для проверки.

    Returns:
        function: Обертка над функцией, которая выполняет проверку значения аргумента.

    Raises:
        ValueError: Если значение последнего аргумента функции не находится в заданном списке.

    Examples:
        >>> @check_str(["м", "ж"])
        ... def check_gender(self, gender: str) -> str:
        ...     return gender

        >>> obj = Giraffe('м', 555.153, 2000.153, 456)
        >>> obj.check_gender("м")
        'м'
        >>> obj.check_gender("ж")
        'ж'
        >>> obj.check_gender("другой")
        ValueError: Для метода check_gender используются обозначения из списка: ['м', 'ж']. Введенное значение - другой
    """
    def decorate(func):
        def wrapper(*arg):
            if arg[-1] not in lst:
                raise ValueError(
                    f"Для метода {func.__name__} используются обозначения из списка: {lst}. Введенное значение - {arg[-1]}")
            else:
                ret = list(func(arg[0], arg[-1]))
                return ret[0]

        return wrapper

    return decorate

class Giraffe:
    """
    Класс, представляющий жирафа.

    Attributes:
        gender (str): Пол жирафа.
        weight (int, float): Вес жирафа.
        neck_length (int, float): Длина шеи жирафа.
        spots (int): Количество пятен на теле жирафа.
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
        self.neck_length = self.check_neck_len(neck_length)
        self.spots = self.check_spots(spots)
        self.weight = self.check_weight(weight)
        self.gender = self.check_gender(gender)


    @check_str(["м", "ж"])
    def check_gender(self, gender: str) -> str:
        """
        Проверяет правильность обозначения пола.
        'м' - мужской
        'ж' - женский

        Args:
            gender (str): Пол жирафа.

        Returns:
            str: Пол жирафа.

        Raises:
            ValueError: Если значение переменной gender не является допустимым обозначением пола.
        """
        return gender

    @check(min_num=2000, max_num=3000, units='см')
    def check_neck_len(self, *neck_length: (int, float)) -> (int, float):
        """
        Проверяет правильность длины шеи жирафа.

        Args:
            neck_length (int, float): Длина шеи жирафа.

        Returns:
            (int, float): Длина шеи жирафа.

        Raises:
            ValueError: Если длина шеи выходит за допустимые пределы.
        """
        return neck_length

    @check(min_num=400, max_num=500, units='ед')
    def check_spots(self, *spots: (int, float)) -> (int, float):
        """
        Проверяет правильность количества пятен на теле жирафа.

        Args:
            spots (int): Количество пятен на теле жирафа.

        Returns:
            int: Количество пятен на теле жирафа.

        Raises:
            ValueError: Если количество пятен выходит за допустимые пределы.
        """
        return spots

    @check(min_num=550, max_num=1900, units='кг')
    def check_weight(self, *weight: (int, float)) -> (int, float):
        """
        Проверяет корректность веса жирафа.

        Args:
        - weight: int, вес жирафа

        Returns:
        - int, проверенное значение веса жирафа

        Raises:
        - ValueError, если переданное значение не попадает в указанный диапазон
        """
        return weight

    def eats(self, plant):
        """
        Метод, описывающий питание жирафа.
        """
        pass

    def reproduces_offspring(self):
        """
        Метод, описывающий размножение жирафа.
        """
        pass

    def movement(self):
        """
        Метод, описывающий движение жирафа.
        """
        pass


class Flora:
    """
    Класс, представляющий растительность.

    Attributes:
        variety (str): разновидность растения
        height (int, float): высота растения
        greenery (int, float): количество зелени в процентах
    """

    def __init__(self, variety, height, greenery) -> None:
        self.variety = self.check_variety(variety)
        self.height = self.check_height(height)
        self.greenery = self.check_greenery(greenery)

    @check(min_num=0, max_num=100, units='%')
    def check_greenery(self, *greenery: (int, float)) -> (int, float):
        """
        Проверяет процент зелени на растении

        Args:
            greenery (int, float): Количество зелени на растении в процентах

        Returns:
            (int, float): Проверенное значение greenery

        Raises:
            ValueError: Если процент озеленения выходит за допустимые пределы.
        """
        return greenery

    @check(min_num=0.2, max_num=20, units='м')
    def check_height(self, *height: (int, float)) -> (int, float):
        """
        Проверяет правильность высоты растения

        Args:
            height (int, float): Высота растения.

        Returns:
            (int, float): Проверенная высота растения.

        Raises:
            ValueError: Если высота растения выходит за допустимые пределы.
        """
        return height

    @check_str(["grass", "shrub", "tree"])
    def check_variety(self, variety: str) -> str:
        """
        Проверяет правильность обозначения разновидности растения.
        grass - трава
        shrub - кустарник
        tree - дерево

        Args:
            variety (str): Разновидность растения.

        Returns:
            str: Проверенная разновидность растения.

        Raises:
            ValueError: Если значение переменной gender не является допустимым обозначением пола.
        """
        return variety

    def growing(self):
        '''
        Метод, описывающий рост растения
        '''
        pass

    def vegetative_reproduction(self):
        '''
        Метод, описывающий вегетативное размножение
        '''
        pass

class Weather:
    """
    Класс, представляющий погоду.

    Attributes:
        temperature (str): текущая температура по цельсию
        humidity (int, float): влажность,  в процентах
        precipitation (int, float): осадки, в мм
        cloud_cover (): облачность, в процентах
    """
    def __init__(self, temperature: (int, float), humidity: (int, float), precipitation: (int, float),  cloud_cover: (int, float)) -> None:
        self.temperature = self.check_temperature(temperature)
        self.humidity = self.check_humidity(humidity)
        self.precipitation = self.check_precipitation(precipitation)
        self.cloud_cover = self.check_cloud_cover(cloud_cover)

    @check(min_num=-24, max_num=+58, units='° C')
    def check_temperature(self, *temperature: (int, float)) -> (int, float):
        """
        Проверяет правильность заданной температуры

        Args:
            temperature (int, float): Заданная температура в цельсиях

        Returns:
            (int, float): Проверенная заданная температура в цельсиях.

        Raises:
            ValueError: Если заданная температура выходит за допустимые пределы.
        """
        return temperature

    @check(min_num=10, max_num=90, units='%')
    def check_humidity(self, *humidity: (int, float)) -> (int, float):
        """
        Проверяет правильность заданной влажности в процентах

        Args:
            humidity (int, float): Заданная влажность в процентах

        Returns:
            (int, float): Проверенная заданная влажность в процентах

        Raises:
            ValueError: Если заданная влажность выходит за допустимые пределы.
        """
        return humidity

    @check(min_num=2, max_num=15, units='мм')
    def check_precipitation(self, *precipitation: (int, float)) -> (int, float):
        """
        Проверяет правильность заданного количества осадков в мм

        Args:
            precipitation (int, float): Заданное количество осадков в мм

        Returns:
            (int, float): Проверенное заданное количество осадков в мм

        Raises:
            ValueError: Если заданное количество осадков выходит за допустимые пределы.
        """
        return precipitation


    @check(min_num=0, max_num=90, units='%')
    def check_cloud_cover(self, *cloud_cover: (int, float)) -> (int, float):
        """
        Проверяет правильность заданное значение: облачность в процентах

        Args:
            cloud_cover (int, float): Заданное значение

        Returns:
            (int, float): Проверенное заданное значение

        Raises:
            ValueError: Если заданное значение выходит за допустимые пределы.
        """
        return cloud_cover


    def solar_energy(self):
        """
        Рассчитывает количество солнечной энергии, получаемой в данной погоде.

        Returns:
            float: количество солнечной энергии в джоулях
        """
        pass

    def wind(self):
        """
        Определяет скорость ветра в данной погоде.

        Returns:
            int,  float: скорость ветра в м/с
        """
        pass

    def weather_conditions(self):
        """
        Определяет общие погодные условия на основе текущих показателей.

        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    tomas = Giraffe('м', 555.153, 2000.153, 456)
    print(tomas.neck_length, tomas.gender)

    acacia = Flora("tree", 16, 70)
    print(acacia.greenery)

    weather = Weather(+40, 30, 5, 50)
    print(weather.temperature)