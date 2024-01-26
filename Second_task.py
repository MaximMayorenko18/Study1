import random
def get_numbers_ticket(min, max, quantity):
    try:
        set_numbers = list(set(random.sample(range(min, max), quantity)))
        print(set_numbers)
    except ValueError:
        return 'Pls enter correct vallue'  

get_numbers_ticket(1, 49,6)  
