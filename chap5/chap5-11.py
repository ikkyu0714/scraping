import requests
import json
from datetime import datetime, timedelta, timezone

url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="36f5c2203a12b7ae2331c917184c3e3b")

jsondata = requests.get(url).json()
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    print("日時:{jst}, 天気:{weather}, 温度:{temp}度".format(jst=jst, weather=weather, temp=temp))