class Book:
    def __init__(self, id_,  name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'{__class__.__name__}({self.name})'


    def __repr__(self):
        return f'{__class__.__name__}({self.id_}, {self.name}, {self.pages})'



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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
    print(type(list_books[0]), list_books[0])
    print(type(list_books[1]), list_books[1])
    book1 = list_books[1]
    print(type(book1), f'book1 = {book1}')