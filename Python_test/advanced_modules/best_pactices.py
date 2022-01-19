import datetime
import pytz

iso_format_string = '%Y-%m-%dT%H:%M:%S%z' 

now_utc = datetime.datetime.now(pytz.timezone('UTC'))
now_eu_kiev = now_utc.astimezone(pytz.timezone('Europe/Kiev'))
now_eu_istanbul = now_utc.astimezone(pytz.timezone('Europe/Istanbul'))

# print(now_utc.strftime(iso_format_string))
# print(now_eu_kiev.strftime(iso_format_string))
# print(now_eu_istanbul.strftime(iso_format_string))
# print(datetime.datetime.utcnow().strftime(iso_format_string))

naive_now = datetime.datetime.now() # .utcnow and no brainsex
print(naive_now.strftime(iso_format_string))
kiev_tz = pytz.timezone('Europe/Kiev')
print(kiev_tz.localize(naive_now))


# [print(tz_) for tz_ in pytz.all_timezones]