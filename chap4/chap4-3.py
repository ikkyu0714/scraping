import pandas as pd

# データフレームを読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")

# 「8」の列が四谷の住所を抽出して表示
result = df[df[8] == "四谷"]
print(result[[2,6,7,8]])

# 「8」の列が四谷の文字が含まれる住所を抽出して表示
result = df[df[8].str.contains("四谷")]
print(result[[2,6,7,8]])