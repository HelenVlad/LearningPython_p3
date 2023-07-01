import random
import hashlib
import re
from generator import data_generator


class IdCounter:
    """
    Класс, в котором хранится генератор значений id (обычный инкремент на 1)
    """

    def __init__(self):
        self._id = 0

    def next_id(self):
        self._id += 1
        return self._id

    def previous_id(self):
        self._id -= 1
        return self._id

    def current_id(self):
        return self._id

    def reset(self):
        self._id = 0


class Password:
    """
    Класс, который ответственен за выдачу хэш-значения пароля и проверке пароля с его хэш значением
    """

    @classmethod
    def get(cls, password: str):
        """
        Функция, которая выдает хэш-значение переданного пароля
        """
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid(password):
        """
        Функция, которая проверяет переданный пароль на валидность.
        Пароль должен:
        1) Содержать латинские прописные и строчные буквы, цифры;
        2) Иметь не менее 8 знаков.
        :param password: Пароль
        :return: True - если проверка пройдена,
        raise TypeError('Пароль не соответствует требованиям') - если нет
        """
        # pattern = re.compile(r'[0-9a-zA-Z][^\s]*')
        pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$')
        if re.fullmatch(pattern, password) and len(password) >= 8:
            return True
        else:
            raise TypeError('Пароль не соответствует требованиям')

    @classmethod
    def check(cls, password: str, hash_password: str) -> bool:
        """
        Проверяет, соотносится ли передаваемый пароль с его хэш-значением
        :param password: Пароль
        :param hash_password: Хэш-значение
        :return: True - если совпадает, False - если не совпадает
        """
        if hashlib.sha256(password.encode()).hexdigest() == hash_password:
            return True
        else:
            return False


COUNTER_FOR_PRODUCT = IdCounter()


class Product:
    """
    Класс, в котором хранится информация о продукте
    """

    def __init__(self, name, price, rating):
        self._id = COUNTER_FOR_PRODUCT.next_id()
        self._name = self.check_attribute(name, str)
        self.price = price
        self.rating = rating

    def __getattribute__(self, item):
        if item == 'id':
            return super().__getattribute__('_id')
        if item == 'name':
            return super().__getattribute__('_name')
        if item in ['price', 'rating']:
            return super().__getattribute__(item)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key in ['price', 'rating']:
            super().__setattr__(key, self.check_attribute(value, (int, float)))
        elif key in ['_name', '_id']:
            super().__setattr__(key, value)
        elif key in ['name', 'id']:
            raise AttributeError(f'Атрибут "{key}" изменить нельзя')
        else:
            raise AttributeError(f'Атрибут {key} не найден.')
        # object.__setattr__(self, key, value)

    @staticmethod
    def check_attribute(value, types):
        if isinstance(value, types):
            return value
        else:
            raise ValueError(f'Недопустимый тип данных. Требуется значение типа {types}.')

    def __str__(self):
        return f'{self._id}_[{self._name}]'

    def __repr__(self):
        return f"{__class__.__name__}(name={self._name!r}, price={self.price}, rating={self.rating!r})"

    @classmethod
    def obj_generator(cls):
        objec = cls(*next(data_generator()))
        return objec


class Cart:
    """
    Корзина, в которой хранится информация о списке товаров
    """

    def __init__(self):
        self._lst = []

    @property
    def lst(self):
        return self._lst

    def checklist(self):
        num = 1
        print(f' № ....Наименование - Цена - Рейтинг')
        for prod in self._lst:
            print(f'{num})....{prod.name} - {prod.price}руб. - {prod.rating}%')
            num += 1

    def __setattr__(self, key, value):
        if key in ['_lst']:
            super().__setattr__(key, value)
        elif key in ['lst']:
            raise AttributeError(f'Атрибут "{key}" изменить нельзя')
        else:
            raise AttributeError(f'Атрибут {key} не найден.')

    def __str__(self):
        return f'{self._lst}'

    def __repr__(self):
        return f"{__class__.__name__}({self._lst})"

    def add(self, *obj_product):
        self._lst.extend(obj_product)

    def del_prod(self, obj_product):
        self._lst.remove(obj_product)


COUNTER_FOR_USER = IdCounter()


class User:
    """
    Класс, в котором хранятся данные о пользователе.
    """

    def __init__(self, username, password):
        self._id = COUNTER_FOR_USER.next_id()
        self._basket = Cart()
        self._password = password
        self._username = Product.check_attribute(username, str)

    def __getattribute__(self, item):
        if item == 'id':
            return super().__getattribute__('_id')
        if item == 'basket':
            return super().__getattribute__('_basket')
        if item == 'username':
            return super().__getattribute__('_username')
        if item == 'password':
            return "Доступ запрещен"

        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key in ['_basket', '_username', '_id']:
            super().__setattr__(key, value)
        elif key in ['basket', 'username', 'id']:
            raise AttributeError(f'Атрибут "{key}" изменить нельзя')
        elif key in ['_password', 'password']:
            value = Password.get(value)
            super().__setattr__(key, value)
        else:
            raise AttributeError(f'Атрибут {key} не найден.')
        # object.__setattr__(self, key, value)

    def __str__(self):
        return f'{self._id}_{self._username}'

    def __repr__(self):
        return f"{__class__.__name__}(username= {self._username}, password= 'password1')"


class Store:
    def __init__(self) -> None:
        self.new_user_ = None
        self.new_user()

    def new_user(self) -> None:
        """
        Аутентификация (чтобы не хранить список пользователей, под аутентификацией будем понимать создание пользователя)
        пользователя через консоль (логин и пароль будут вводиться через консоль)
        Устанавливается атрибут self.new_user_
        :return: None
        """
        self.new_user_ = User(input('Введите имя пользователя:\n-->'),
                              input('Введите пароль для защиты учетной записи:\n-->'))

    def add_to_basket(self, num=1) -> None:
        """
        Метод, позволяющий пользователю добавить (по умолчанию один) случайный продукт в корзину
        :param num: количество случайно помещаемых продуктов
        :return: None
        """
        for ix in range(num):
            self.new_user_._basket.add(Product.obj_generator())

    def view_to_cart(self) -> None:
        """
        Метод, позволяющий пользователю просмотреть свою корзину

        :return: None
        """
        self.new_user_._basket.checklist()


if __name__ == '__main__':

    main = Store()
    main.add_to_basket(10)
    main.view_to_cart()

