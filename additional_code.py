# parser.add_argument("--chosen_day", type=str, help="Выбранная дата", default=date.today().strftime('%Y-%m-%d'))
# parser.add_argument("--chosen_week_start", type=str, help="Начало выбранной недели", default=date.today().strftime('%Y-%m-%d'))
# parser.add_argument("--chosen_week_finish", type=str, help="Конец выбранной недели", default=(date.today() + pd.Timedelta(days=7)).strftime('%Y-%m-%d'))

# try:
#     chosen_day = datetime.strptime(args.chosen_day, '%Y-%m-%d')
# except ValueError:
#     print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
#     exit(1)

# try:
#     chosen_week_start_date = datetime.strptime(args.chosen_week_start, '%Y-%m-%d')
# except ValueError:
#     print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
#     exit(1)

# try:
#     chosen_week_finish_date = datetime.strptime(args.chosen_week_finish, '%Y-%m-%d')
# except ValueError:
#     print("Ошибка: Формат даты должен быть ГГГГ-ММ-ДД, например, '1945-05-09'")
#     exit(1)


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

