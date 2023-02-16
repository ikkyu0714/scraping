import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df1 = pd.read_csv("Preview_20230210202859.csv", header = 1, index_col = "時点")

df1["年平均気温【℃】"].plot()
plt.ylim(-10, 40)
plt.show()