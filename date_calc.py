'''Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату'''

import logging
import datetime
import calendar
import argparse

logging.basicConfig(level=logging.NOTSET, filename='date_calc.log', filemode='w', encoding='utf-8')
logger = logging.getLogger()


def date_calc(input_text):
    words = input_text.split()
    find_num_day = 6
    try:
        find_num_day = int(words[0][0])
    except ValueError as e:
        logger.error(e)
    if find_num_day > 5:
        logger.error('Number of day of week must be integer from 1 to 5')
    find_week_day = words[1].capitalize()
    if not find_week_day in list(calendar.day_name):
        logger.error('Day of the week entry error')
    find_month = words[-1].capitalize()
    if not find_month in list(calendar.month_name):
        logger.error('Month entry error')

    year = datetime.datetime.now().year
    current_date = datetime.datetime.strptime(f'{year} {find_month} 1', '%Y %B %d')
    delta_day = datetime.timedelta(hours=24)
    counter_matching = 0
    while current_date.strftime('%B') == find_month:
        if current_date.strftime('%A') == find_week_day:
            counter_matching += 1
            if counter_matching == find_num_day:
                break
        current_date += delta_day
    if counter_matching < find_num_day:
        logger.info(f"No {find_num_day} {find_week_day}s in {find_month}")
        print(f"No {find_num_day} {find_week_day}s in {find_month}")
    else:
        logger.info(current_date)
        print(current_date)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='date text parser')
    parser.add_argument(
        'text', metavar='input_text', type=str, nargs='?',
        help='Enter which day of month would you like to find',
        default='1st Monday of January'
        )

    args = parser.parse_args()
    date_calc(args.text)
