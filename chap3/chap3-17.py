import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読みこむ
df = pd.read_csv("test.csv", index_col=0)

# 棒グラフを作って表示する
df.T.plot.bar()
plt.legend(loc="lower right")
plt.show()
