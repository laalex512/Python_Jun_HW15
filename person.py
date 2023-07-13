'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.'''
import argparse
import logging

from my_exceptions import PersonNameError, PersonAgeError


class Person:
    def __init__(self, full_name, age, city='Minsk'):
        self.full_name = full_name
        self.__age = age
        self.city = city

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'{self.full_name}: {self.__age} years old from {self.city}'


def check_fullname(text: str):
    """Простенькая проверка имени на количество слов - возврат -1;
     заглавную первую, остальные прописные, отсутствие цифр - возврат номера слова с ошибкой;
     если все норм - возврат 0
     """

    words = text.split()
    if len(words) < 2:
        return -1
    for number, word in enumerate(words, 1):
        if word[0].islower() or word[0].isdigit():
            return number
        for i in range(1, len(word)):
            if word[i].isupper() or word[i].isdigit():
                return number
    return 0


if __name__ == '__main__':
    LOG_FORMAT = '{asctime} - {levelname}: {msg}'

    parser = argparse.ArgumentParser(description='date text parser')
    parser.add_argument(
        '-name', metavar='fullname of Person', type=str, nargs='?',
        help='Enter fullname of Person',
        default='John Snow'
        )
    parser.add_argument(
        '-age', metavar="Person's age", type=str, nargs='?',
        help="Enter Person's age",
        default='30'
        )
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.NOTSET, filename='person.log', filemode='w', encoding='utf-8', style='{',
        format=LOG_FORMAT
        )
    logger = logging.getLogger()

    name = args.name
    if check_fullname(name):
        logger.error('PersonNameError')
        raise PersonNameError(check_fullname(name))
    try:
        age = int(args.age)
    except ValueError:
        logger.error('PersonAgeError')
        raise PersonAgeError(-1)
    if age < 0:
        logger.error('PersonAgeError')
        raise PersonAgeError(1)
    person1 = Person(name, age)
    logger.info(person1)
    print(person1)
