import pytz
import datetime


while True:
	user_input = input('Please enter a two-letter code of the country to choose timezone or press "q" to quit: ').upper()
	if user_input == 'Q':
		break
	print('\n\n',datetime.datetime.utcnow(),'  UTC\n')

	for time_zone in pytz.country_timezones[user_input]:
		print(datetime.datetime.now(pytz.timezone(time_zone)),f'{time_zone}')