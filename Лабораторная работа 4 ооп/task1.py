from typing import Union
import doctest

if __name__ == "__main__":
    class Cars:
        MIN_SPEED = 20

        def __init__(self, stamp: str, title: str):
            """
           Создание и подготовка к работе объекта "Автомобиль"

           :param title: Название автомобиля
           :param stamp: Марка автомобиля

           Примеры:
           >>> BMW = Cars("BMW", "X5")  # инициализация экземпляра класса
           """
            if not isinstance(stamp, str):
                raise TypeError("Введите строку ")
            else:
                self.stamp = stamp

            if not isinstance(title, str):
                raise TypeError("Введите строку")
            else:
                self.title = title

        def __str__(self):
            """
            Функция возвращает представление класса
            >>>BMW = Cars("BMW", "X5")  # инициализация экземпляра класса
            >>>print(BMW)
            """
            return f" Марка автомобиля: {self.stamp}. Название: {self.title}"

        def __repr__(self):
            """
            Функция возвращает валидную строку
            >>>BMW = Cars("BMW", "X5")  # инициализация экземпляра класса
            >>>print(repr(BMW))
            "Cars("BMW", "X5")"
            """
            return f"{self.__class__.__name__}({self.stamp}, {self.title}) "

        def start(self) -> None:
            """
           Функция возвращает строрку с информацией о запуске машины
           >>>BMW = Cars("BMW", "X5")  # инициализация экземпляра класса
           >>>BMW.start()
           """
            print(f"{self.stamp} {self.title} готова к работе")

        def drive(self) -> None:
            """
           Функция возвращает строрку с информацией о запуске машины
           >>>BMW = Cars("BMW", "X5")  # инициализация экземпляра класса
           >>>BMW.drive()
           """
            print(f"Автомобиль поехал с минимальной скоростью: {self.MIN_SPEED}")


    class Trucks(Cars):
        def __init__(self, stamp: str, title: str, payload: Union[int, float]):
            """
           Создание и подготовка к работе объекта "Автомобиль"

           :param title: Название автомобиля
           :param stamp: Марка автомобиля
           :param payload: Полезная нагрузка

           Примеры:
           >>> BMW = Trucks("BMW", "X5", 23000)  # инициализация экземпляра класса
           """
            if not isinstance(payload, (int, float)):
                raise TypeError("Нагрузка должна быть типа int или float ")
            else:
                self.payload = payload
            super().__init__(stamp, title)
            self.current_load = 0

        def add_weight(self, weight: Union[int, float]) -> None:
            """
           Функция управляет текущей полезной нарузкой
           >>>BMW = Trucks("BMW", "X5",23000)  # инициализация экземпляра класса
           >>>BMW.add_weight(1000)
           """
            if self.payload > self.current_load + weight:
                self.current_load += weight
                print(f"В машину загруженно {self.current_load} кг")
            else:
                raise ValueError("Машина будет перегружена!!!")

        def drive(self) -> None:
            """
           Функция запускает движение автомобиля с определенной скоростью.У разных типов автомобилей разная скорсоть
           >>>BMW = Trucks("BMW", "X5",23000)  # инициализация экземпляра класса
           >>>BMW.drive()
           """
            print(f"Автомобиль поехал со скоростью: {self.MIN_SPEED + 20}")

        def __repr__(self):
            """
            Функция возвращает валидную строку
            >>>BMW = Trucks("BMW", "X5",23000)  # инициализация экземпляра класса
            >>>print(repr(BMW))
            """
            return f"{self.__class__.__name__}({self.stamp}, {self.title}, {self.payload})"


    class Motorcar(Cars):
        def __init__(self, stamp: str, title: str, num_seats: int):
            """
           Создание и подготовка к работе объекта "Автомобиль"

           :param title: Название автомобиля
           :param stamp: Марка автомобиля
           :param num_seats: Количество сидений для пассажиров

           Примеры:
           >>> BMW = Motorcar("BMW", "X5", 5)  # инициализация экземпляра класса
           """
            if not isinstance(num_seats, int):
                raise TypeError("Количество сидений число целое (типа int)")
            elif num_seats < 0:
                raise ValueError("Число должно быть положительным")
            self.num_seats = num_seats
            super().__init__(stamp, title)

        def is_fit(self, people: int) -> bool:
            """
           Функция проверяет поместятся ли пассжиры
           >>>BMW = Motorcar("BMW", "X5", 5)  # инициализация экземпляра класса
           >>>BMW.is_fit(4)
           True
           """
            return True if people <= self.num_seats else False

        def drive(self) -> None:
            """
          Функция печатет сообщение о скорости движения автомобиля. У разных типов автомобилей разная скорсоть
          >>>BMW = Motorcar("BMW", "X5", 5)  # инициализация экземпляра класса
          >>>BMW.drive()

          """
            print(f"Автомобиль поехал со скоростью: {self.MIN_SPEED + 40}")

        def __repr__(self):
            """
           Функция возвращает валидную строку
           >>>BMW = Motorcar("BMW", "X5", 5)  # инициализация экземпляра класса
           >>>print(repr(BMW))
           """
            return f"{self.__class__.__name__}({self.stamp}, {self.title},{self.num_seats})"
