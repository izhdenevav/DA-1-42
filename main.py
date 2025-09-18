from datetime import datetime, date
import argparse

import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument("--date", type=str, help="Начальная дата в формате ГГГГ-ММ-ДД", default=date.today().strftime('%Y-%m-%d'))
parser.add_argument("--freq", type=str, help="Частота", default='D')
parser.add_argument("--period", type=int, help="Количество дат", default=30)
parser.add_argument("--chosen_day", type=str, help="Выбранная дата", default=date.today().strftime('%Y-%m-%d'))
parser.add_argument("--chosen_week_start", type=str, help="Начало выбранной недели", default=date.today().strftime('%Y-%m-%d'))
parser.add_argument("--chosen_week_finish", type=str, help="Конец выбранной недели", default=(date.today() + pd.Timedelta(days=7)).strftime('%Y-%m-%d'))
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

try:
    chosen_day = datetime.strptime(args.chosen_day, '%Y-%m-%d')
except ValueError:
    print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
    exit(1)

try:
    chosen_week_start_date = datetime.strptime(args.chosen_week_start, '%Y-%m-%d')
except ValueError:
    print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
    exit(1)

try:
    chosen_week_finish_date = datetime.strptime(args.chosen_week_finish, '%Y-%m-%d')
except ValueError:
    print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
    exit(1)

# создаем массив из введенного количества дат с введенной частотой, начиная с введенной даты
dates = pd.date_range(start=start_date, periods=args.period, freq=args.freq)

# создаем датафрейм, в качестве индекса - наш массив дат
df = pd.DataFrame({
    'value': range(args.period)
}, index=dates)

# # выбираем данные за введенный день
# chosen_day_info = df.loc[chosen_day]

# # выбираем данные за введенную неделю
# chosen_week_info = df.loc[chosen_week_start_date:chosen_week_finish_date]

# print("-------------------------------------------------------------")
# print(f"Данные за {chosen_day}: ")
# print(chosen_day_info)
# print("-------------------------------------------------------------")
# print(f"Данные за неделю с {chosen_week_start_date} по {chosen_week_finish_date}: ")
# print(chosen_week_info)
# print("-------------------------------------------------------------")

# отрисовываем график для датафрейма, ось х для дат и ось у для значений
plt.plot(df.index, df['value'], marker='o')
plt.grid(True)
plt.xticks(rotation=60)
plt.tight_layout()
# график сохраняем в введенный файл
plt.savefig(f'{args.filename}.png')
plt.close()

print(f"График сохранён в файл '{args.filename}.png'")