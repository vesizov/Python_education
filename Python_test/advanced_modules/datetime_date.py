from datetime import date
today = date.today()
# print(today)
# print(f"{today.day}-{today.month}-{today.year}")

# date_1 = date(2021,12,3)
# date_2 = date(2021,3,3)

# diff = date_1 - date_2
# print(diff)

# my_bd = date(today.year if today < date(today.year, 1, 30) else today.year+1, 1, 30)
# print((my_bd - today).days)

print(today.weekday())
print(today.isoweekday())