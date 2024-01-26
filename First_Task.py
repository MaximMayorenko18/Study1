import datetime 
def get_days_from_today(date):
    try:
        #змінна яка приймає відформатоване значення
        get_date = datetime.datetime.strptime(date,'%Y-%m-%d').date()
        # Сьогодні)
        today = datetime.date.today()
        #Різниця
        difference =  today - get_date
        return difference.days 
    except ValueError:
        return 'Неправельний формат дати'
    
print(get_days_from_today("2020-10-09"))    