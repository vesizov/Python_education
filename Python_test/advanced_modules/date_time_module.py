import pytz
import datetime

# kiev  = 'Europe/Kiev'
thailand = 'Asia/Bangkok'
# tz_kiev = pytz.timezone(kiev)
tz_thailand = pytz.timezone(thailand)
# kiev_time = datetime.datetime.now(tz=tz_kiev)
thailand_time = datetime.datetime.now(tz_thailand)
# print(kiev_time)
print(thailand_time)

# [print(tz) for tz in pytz.all_timezones]
# [print(country, pytz.country_names.get(country), pytz.country_timezones.get(country)) for country in pytz.country_names]
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
