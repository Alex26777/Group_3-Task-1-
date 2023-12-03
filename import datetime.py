import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    """
    Виводить імена людей, у яких день народження в поточному тижні.

    :param users: список словників з ключами 'name' та 'birthday'
    """
    today = datetime.date.today()
    # Визначаємо понеділок поточного тижня
    start_of_week = today - datetime.timedelta(days=today.weekday())
    # Визначаємо неділю поточного тижня
    end_of_week = start_of_week + datetime.timedelta(days=6)
    birthdays_this_week = defaultdict(list)

    for user in users:
        name = user['name']
        # Конвертуємо datetime в date для порівняння
        birthday = user['birthday'].date()
        # Встановлюємо рік дня народження як поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        # Перевіряємо, чи день народження випадає на поточний тиждень
        if start_of_week <= birthday_this_year <= end_of_week:
            # Отримуємо назву дня тижня
            weekday = birthday_this_year.strftime('%A')
            # Додаємо ім'я до відповідного дня тижня
            birthdays_this_week[weekday].append(name)
    
    # Виводимо імена по днях тижня
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']:
        if birthdays_this_week[day]:
            # Виводимо імена, які мають бути виведені в консоль
            print(f'{day}: {", ".join(birthdays_this_week[day])}')

# Приклад використання
users = [
    {'name': 'Білл Гейтс', 'birthday': datetime.datetime(1955, 10, 28)},
    # Додайте сюди більше записів про користувачів
]

get_birthdays_per_week(users)
