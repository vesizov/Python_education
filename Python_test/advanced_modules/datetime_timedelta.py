from datetime import timedelta, datetime

print(datetime.now()+timedelta(days=333))


lb = datetime(2021,1,30)
print((datetime.now() - lb).days)