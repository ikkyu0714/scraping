import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読みこむ
df = pd.read_csv("test.csv", index_col=0)

# 棒グラフを作って表示する
colorlist = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
plt.savefig("bargraph.png")
