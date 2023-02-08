import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("../test.csv")

# １列のデータを表示
print("Cのデータ\n", df.loc[2])

# 複数の行のデータを表示
print("CとDのデータ\n", df.loc[[2,3]])

# 複数の行のデータを表示
print("Cの国語データ\n", df.loc[2]["国語"])