
class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if pages < 0:
            raise ValueError("Количество страниц должно быть больше нуля!")
        elif not isinstance(pages, int):
            raise TypeError
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if duration < 0:
            raise ValueError("Продолжительность должна быть больше нуля!")
        elif not isinstance(duration, float):
            raise TypeError
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.duration})"


Audio = AudioBook("Ад в небеса", "Толстой ", 1.23)
print(Audio)
