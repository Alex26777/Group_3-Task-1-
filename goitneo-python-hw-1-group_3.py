from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    today = datetime.today()
    weekdays = {i: [] for i in ['Monday', 'Tuesday', 'Wednesday',
                                'Thursday', 'Friday', 'Saturday', 'Sunday']}

    for user in users:
        name = user['name']  # Ім'я користувача.
        # Дата народження у поточному році.
        birthday = user['birthday'].replace(year=today.year)

        # Якщо день народження вже пройшов цього року, дивимося наступний рік.
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Різниця днів між днем народження та сьогоднішнім днем.
        delta = birthday - today
        if 0 <= delta.days <= 7:
            # Якщо день народження на вихідні, переносимо на понеділок.
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                birthday = birthday + timedelta(days=(7 - birthday.weekday()))
            # Додаємо ім'я до відповідного дня тижня.
            weekdays[birthday.strftime('%A')].append(name)

    # Виведення результатів.
    for day in weekdays:
        if weekdays[day]:
            print(f"{day}: {', '.join(weekdays[day])}")


# Тестування функції.
users = [
    {"name": "Alice", "birthday": datetime(1990, 12, 17)},
    # Додайте інших користувачів тут.
]

get_birthdays_per_week(users)
