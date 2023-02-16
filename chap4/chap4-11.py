import pandas as pd

# データフレームを読み込む
df1 = pd.read_csv("Preview_20230210202859.csv", header = 1, index_col = "時点")
df2 = pd.read_csv("Preview_20230210202916.csv", header = 1, index_col = "時点")
df3 = pd.read_csv("Preview_20230210202925.csv", header = 1, index_col = "時点")

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)