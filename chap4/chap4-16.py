import pandas as pd

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift-jis")

hydrant = df[["緯度", "経度"]].values
print(len(hydrant))
print(hydrant)