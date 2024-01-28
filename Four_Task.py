from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta = (birthday_this_year - today).days

    
        if 0 <= delta <= 7:
        
            if birthday_this_year.weekday() in [5, 6]: 
                days_to_monday = 7 - birthday_this_year.weekday()
                birthday_this_year += timedelta(days=days_to_monday)
            
            
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
    {"name": "Anna", "birthday": "1990.01.29"},
    {"name": "Max", "birthday": "1988.09.12"},
   
]

print(get_upcoming_birthdays(users))
