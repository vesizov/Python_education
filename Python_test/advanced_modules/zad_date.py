from datetime import date

user_input = tuple(map(int, input('Enter the date (yyyy-mm-dd): ').strip().split('-')))
user_day = date(*user_input)
#week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(f"That is {user_day.strftime('%A')}") #week[user_day.weekday()]
