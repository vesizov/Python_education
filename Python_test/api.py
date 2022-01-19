import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params = {
'format' : 'geojson',
'starttime' : '2021-01-01',
'endtime' : '2021-03-02',
'longitude' : '55.3',
'latitude' : '86.08',
'maxradiuskm' : '2000'
	})
# print(response.text)
# print(response.json())
data = response.json()['features'][0]['properties']['place']
# print(data,'\n \n')

for i in response.json()['features']:
	print(i['properties']['place'])