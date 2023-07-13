class MyException(Exception):
    pass


class RectangleException(MyException):
    pass


class RectangleNotNumberError(RectangleException):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Сторона {self.side} введена неправильно. Сторона должна быть вещественным числом'


class RectangleLowerNullError(RectangleException):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0:
            return f'Сторона а введена неправильно. Сторона должна быть положительным числом'
        else:
            return f'Сторона b введена неправильно. Сторона должна быть положительным числом'


class PersonException(MyException):
    pass


class PersonNameError(PersonException):
    def __init__(self, error_code):
        self.error_code = error_code

    def __str__(self):
        if self.error_code < 0:
            return f'Ошибка. Полное имя должно состоять минимум из двух слов'
        else:
            return f'Ошибка в {self.error_code}-м слове. Каждое слово в имени должно начинаться с' \
                   f' заглавной буквы, остальные буквы должны быть строчными, не должно быть цифр'


class PersonAgeError(PersonException):
    def __init__(self, error_code):
        self.error_code = error_code

    def __str__(self):
        if self.error_code < 0:
            return f'Ошибка. Возраст должен быть описан целым числом'
        else:
            return f'Ошибка. Возраст должен быть положительным числом'
