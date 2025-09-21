from datetime import datetime, date
import argparse

from dategraphic import DateGraphic

parser = argparse.ArgumentParser()

parser.add_argument("--date", type=str, help="Начальная дата в формате ГГГГ-ММ-ДД", default=date.today().strftime('%Y-%m-%d'))
parser.add_argument("--freq", type=str, help="Частота", default='D')
parser.add_argument("--period", type=int, help="Количество дат", default=30)
parser.add_argument("--filename", type=str, default=f"date_graphic_{date.today().strftime('%Y-%m-%d')}")

args = parser.parse_args()  

try:
    start_date = datetime.strptime(args.date, '%Y-%m-%d')
except ValueError:
    print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
    exit(1)

valid_freqs = ['D', 'H', 'T', 'S', 'W', 'M']
if args.freq not in valid_freqs:
    print(f"Ошибка: Частота может быть {valid_freqs}")
    exit(1)

if args.period <= 0:
    print(f"Ошибка: Введите адекватное количество дат, пожалуйста")
    exit(1)

dategraphic = DateGraphic(start_date, args.freq, args.period, args.filename)
dategraphic.save_graphic()