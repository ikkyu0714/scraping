import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd

url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="36f5c2203a12b7ae2331c917184c3e3b")

jsondata = requests.get(url).json()
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    temp = dat["main"]["temp"]
    df.loc[jst] = temp
pprint(df)