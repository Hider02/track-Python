from typing import Any

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

if __name__ == '__main__':
    class Book:
        def __init__(self, id_, name, pages):
            self.id = id_
            self.name = name
            self.pages = pages

        def __str__(self):
            return f"Книга \"{self.name}\""

        def __repr__(self):
            return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


    class Library:
        def __init__(self, books=None):
            if books is None:
                self.books = []
            else:
                self.books = books.copy()

        def get_next_book_id(self) -> int:
            return len(self.books) + 1

        def get_index_by_book_id(self, id: Any) -> ValueError | int:
            for index, value in enumerate(self.books):
                if value.id == id:
                    return index
            return ValueError("Книги с запрашиваемым id не существует")


    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
