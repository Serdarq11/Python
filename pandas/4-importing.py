import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

# CSV: Comma Seperated Values
# JSON: JavaScript Object Notation

df = pd.read_csv("data.csv")
# df = pd.read_json("pandas/data.json") # and this is for json files

# print(df)   # first and last 5 rows
print(df.to_string())   # all rows

