import argparse
import logging

from my_exceptions import RectangleLowerNullError, RectangleNotNumberError


class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: float, b: float = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'


if __name__ == '__main__':
    LOG_FORMAT = '{asctime} - {levelname}: {msg}'

    parser = argparse.ArgumentParser(description='date text parser')
    parser.add_argument(
        '-a', metavar='side a of rectangle', type=int, nargs='?',
        help='Enter side a of rectangle',
        default=5
        )
    parser.add_argument(
        '-b', metavar="side b of rectangle", type=int, nargs='?',
        help="Enter side b of rectangle",
        default=5
        )
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.NOTSET, filename='rectangle.log', filemode='w', encoding='utf-8', style='{',
        format=LOG_FORMAT
        )
    logger = logging.getLogger()
    try:
        a = float(args.a)
    except ValueError:
        logger.error('RectangleNotNumberError')
        raise RectangleNotNumberError('a')
    try:
        b = float(args.b)
    except ValueError:
        logger.error('RectangleNotNumberError')
        raise RectangleNotNumberError('b')
    if a <= 0 or b <= 0:
        logger.error('RectangleLowerNullError')
        raise RectangleLowerNullError(a, b)
    else:
        rect_1 = Rectangle(a, b)
    logger.info(rect_1)
    print(rect_1)
