import requests
import sqlite3

# starttime = input('Enter start time please (YYYY-MM-DD): ')
# endtime = input('Enter end time please (YYYY-MM-DD): ')
# latitude = input('Enter the latitude please: ')
# longitude = input('Enter the longitude please: ')
# maxradiuskm = input('Enter search radius in kilometers please: ')
# minmagnitude = input('Enter mim magnitude please: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params = {
# 'format' : 'geojson',
# 'starttime' : starttime,
# 'endtime' : endtime,
# 'longitude' : longitude,
# 'latitude' : latitude,
# 'maxradiuskm' : maxradiuskm,
# 'minmagnitude' : minmagnitude 
'format' : 'geojson',
'starttime' : '2021-01-01',
'endtime' : '2021-03-02',
'longitude' : '55.3',
'latitude' : '86.08',
'maxradiuskm' : '2000',
'minmagnitude' : '2'
	})

data = response.json()['features']
print('\n \n')

connection = sqlite3.connect('earthquake_db.db')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL);")


for i, earthquake in enumerate(data):
	print(i+1,' Place: ', earthquake['properties']['place'],' Magnitude: ', earthquake['properties']['mag'])

gen_place = (earthquake['properties']['place'] for earthquake in data)
gen_mag = (earthquake['properties']['mag'] for earthquake in data)

cursor.executemany("INSERT INTO earthquakes VALUES (?,?)", (value for value in zip(gen_place, gen_mag))) #extreme generating

connection.commit()
connection.close()