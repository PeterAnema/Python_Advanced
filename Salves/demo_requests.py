import requests

appid = 'd1526a9039658a6f76950cff21823aff'

url_base = 'http://api.openweathermap.org/data/2.5/weather'

city = 'Amsterdam'

url = f'{url_base}?units=metric&appid={appid}&q={city}'

print(url)

response = requests.get(url)

requests.po

print('status code:', response.status_code)

if response.status_code == 200:

    r = response.json()
    print(r)

    print( f"In {city} is het nu {round(r['main']['temp'])}\u00B0. {r['weather'][0]['description']}.")

    lon = r['coord']['lon']
    lat = r['coord']['lat']

    assert (lon, lat) == (4.8897, 52.3)

else:
    print('Cannot connect to url')