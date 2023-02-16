import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_230210172747.csv", index_col = "全国・都道府県", encoding="shift_jis")

df["2021年"] = pd.to_numeric(df["2021年"].str.replace(",", ""))
print(df["2021年"])
# 2021年の列データで棒グラフを作って表示する
df["2021年"].plot.bar()
plt.show()
