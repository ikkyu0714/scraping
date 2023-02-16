import pandas as pd

# データフレームを読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")

# 「２」の列が「1600006」の住所を抽出して表示
result = df[df[2] == 1600006]
print(result[[2,6,7,8]])