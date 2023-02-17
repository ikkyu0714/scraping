import json
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
url = url.format(city="New York,US", key="36f5c2203a12b7ae2331c917184c3e3b")

jsondata = requests.get(url).json()
print("都市名 = ", jsondata["name"])
print("気温 = ", jsondata["main"]["temp"])
print("天気 = ", jsondata["weather"][0]["main"])
print("天気 = ", jsondata["weather"][0]["description"])
