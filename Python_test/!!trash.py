import requests
from requests import HTTPError
print('hi')
for url in ["https://www.engineerspock.com/", "https://www.engineerspock.com/qweqw"]:
    try:
        response = requests.get(url)
        
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error:{http_err}')
    except Exception as err:
        print('Unknown error')
    else:
        print('Ok')