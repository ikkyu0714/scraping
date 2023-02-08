import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("../test.csv")

# １列のデータを追加
df["美術"] = [68, 73, 82, 77, 94, 96]
print("列データ（美術）を追加\n", df)

# 1行データを追加
df.loc[6] = ["G", 90, 92, 94, 96,92,98]
print("行データを（G）を追加\n",df)
