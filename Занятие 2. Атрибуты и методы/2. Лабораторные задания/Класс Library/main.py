BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'{__class__.__name__}(id_={self.id_}, name=\'{self.name}\', pages={self.pages})'


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = {i: x for i, x in enumerate(books)}

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, idd):

        for x in self.books.items():
            if x[-1].id_ == idd:
                return x[0]
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
