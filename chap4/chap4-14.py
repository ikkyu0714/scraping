import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df1 = pd.read_csv("Preview_20230210202859.csv", header = 1, index_col = "時点")
df2 = pd.read_csv("Preview_20230210202916.csv", header = 1, index_col = "時点")
df3 = pd.read_csv("Preview_20230210202925.csv", header = 1, index_col = "時点")

df1["年平均気温【℃】"].plot()
df2["東京都"].plot()
df3["東京都"].plot()
plt.ylim(-10, 40)
plt.legend(loc="lower right")
plt.show()