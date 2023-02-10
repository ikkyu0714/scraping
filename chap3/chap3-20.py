import pandas as pd
import openpyxl

# CSVファイルを読みこむ
df = pd.read_csv("test.csv")

# ソート（国語の点数が高いもの順）
kokugo = df.sort_values("国語", ascending=False)

# Excelファイルに出力
kokugo.to_excel("csv_to_excel1.xlsx")

