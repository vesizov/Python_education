from datetime import datetime
# today = datetime(2021, 12, 3)
# today_now = datetime.now()

# print(today)
# print(today_now)
# print(datetime.timestamp(today))
# print(datetime.timestamp(datetime.now()))

# timestamp = datetime.timestamp(datetime.now())
# print(datetime.fromtimestamp(timestamp))

# today_format = today.strftime('%d %B %Y')

# print(f"Today is {today_format}")
# print(f"Today is {today.strftime('%A')}")



today = datetime.today()
print(today)
utc_today = today.utcnow()
print(utc_today)
print(today.date())
print(today.time())
print(today.isocalendar())
print(today.isoformat())