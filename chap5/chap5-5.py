import json
import requests
from pprint import pprint

url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
url = url.format(city="Kobe,JP", key="36f5c2203a12b7ae2331c917184c3e3b")

jsondata = requests.get(url).json()
pprint(jsondata)