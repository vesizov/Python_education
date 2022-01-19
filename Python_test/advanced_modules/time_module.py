import time


print(f"UTC time {time.strftime('%Y/%m/%d  %H:%M:%S', time.gmtime())}")
print(f"Local time {time.strftime('%Y/%m/%d  %H:%M:%S', time.localtime())}")

print(time.altzone/60/60)
print(time.daylight)
print(time.timezone/3600)
print()
print(time.tzname)
print(time.localtime().tm_zone)
print(time.localtime().tm_gmtoff)