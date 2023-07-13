class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __setattr__(self, key, value):
        if key == 'pages':
            self.__dict__[key] = self.check_attribute(value, 10, 4000)
        elif key == 'duration':
            self.__dict__[key] = self.check_attribute(value, 10, 4000)
        elif key in ("name", "author"):
            raise AttributeError(f'Атрибут "{key}" изменить нельзя')
        else:
            super().__setattr__(key, value)
        # object.__setattr__(self, key, value)

    @staticmethod
    def check_attribute(value, min_limit, max_limit):
        if isinstance(value, (int, float)) and min_limit < value < max_limit:
            return value
        elif not isinstance(value, (int, float)):
            raise ValueError(f'Недопустимый тип данных. Требуется числовое значение.')
        elif not min_limit < value < max_limit:
            raise ValueError(
                f'Введенное значение не входит в интервал: {min_limit=} < {value} < {max_limit=}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = self.check_attribute(pages, 10, 4000)


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = self.check_attribute(duration, 3, 7000)
