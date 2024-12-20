# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Stack:
    """
    Класс, описывающий стек.
    """

    def __init__(self, max_size: int):
        """
        Создание объекта "Стек".
        :param max_size: Максимальный размер стека.
        Пример:
        >>> stack = Stack(10)
        """
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть положительным числом")
        self.max_size = max_size

    def push(self, item: int) -> None:
        """
        Добавляет элемент в стек.
        :param item: Элемент, который нужно добавить.
        :raise OverflowError: Если стек заполнен.
        Пример:
        >>> stack = Stack(10)
        >>> stack.push(5)
        """
        ...

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека.
        :return: Верхний элемент стека.
        :raise IndexError: Если стек пуст.
        """
        ...


class CPU:
    """
    Класс, описывающий процессор.
    """

    def __init__(self, cores: int, clock_speed: float):
        """
        Создание объекта "Процессор".

        :param cores: Количество ядер процессора.
        :param clock_speed: Частота процессора.
        :raise ValueError: Если количество ядер или частота меньше или равны нулю.

        Пример:
        >>> processor = Processor(8, 3.5)
        """
        if cores <= 0:
            raise ValueError("Количество ядер должно быть положительным числом")
        if clock_speed <= 0:
            raise ValueError("Частота процессора должна быть положительным числом")
        self.cores = cores
        self.clock_speed = clock_speed

    def calculate(self, instructions: int) -> float:
        """
        Выполняет вычисления.

        :param instructions: Количество инструкций.
        :return: Время выполнения в секундах.
        :raise ValueError: Если количество инструкций меньше или равно нулю.

        Пример:
        >>> processor = Processor(8, 3.5)
        >>> processor.calculate(1000000)
        """
        if instructions <= 0:
            raise ValueError
        ...

    def overclock(self, additional_speed: float) -> None:
        """
        Разгоняет процессор.

        :param additional_speed: Дополнительная частота.
        :raise ValueError: Если дополнительная частота меньше или равна нулю.

        Пример:
        >>> processor = Processor(8, 3.5)
        >>> processor.overclock(0.5)
        """
        if additional_speed <= 0:
            raise ValueError
        ...


class RobotVacuumCleaner:
    """
    Класс, описывающий робот-пылесос.
    """

    def __init__(self, battery_capacity: float, dustbin_capacity: float):
        """
        Создание объекта "Робот-пылесос".

        :param battery_capacity: Емкость аккумулятора (в мАч).
        :param dustbin_capacity: Объем пылесборника (в литрах).
        :raise ValueError: Если емкость аккумулятора или объем пылесборника меньше или равны нулю.

        Пример:
        >>> robot = RobotVacuumCleaner(4000, 0.6)
        """
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        if dustbin_capacity <= 0:
            raise ValueError("Объем пылесборника должен быть положительным числом")
        self.battery_capacity = battery_capacity
        self.dustbin_capacity = dustbin_capacity

    def start_cleaning(self) -> None:
        """
        Запускает процесс уборки.

        Пример:
        >>> robot = RobotVacuumCleaner(4000, 0.6)
        >>> robot.start_cleaning()
        """
        ...

    def return_to_base(self) -> None:
        """
        Возвращает робот-пылесос на базу для зарядки.

        Пример:
        >>> robot = RobotVacuumCleaner(4000, 0.6)
        >>> robot.return_to_base()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
