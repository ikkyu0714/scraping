import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む
df = pd.read_csv("../test.csv")

# 棒グラフを作って表示する
df.plot.bar()
plt.legend(loc='lower right')
plt.show()

# 棒グラフ（水平）を作って表示する
df.plot.barh()
plt.legend(loc='lower left')
plt.show()

# 積み上げ棒グラフを作って表示する
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

# 箱ひげグラフを作って表示する
df.plot.box()
plt.show()

# 面グラフを作って表示する
df.plot.area(stacked=True)
plt.legend(loc="lower right")
plt.show()