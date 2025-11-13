import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

# aggregate functions = Reduces a set of values into a single summary value
#                       used to summarize and analyze data
#                       often used with groupby() function

df = pd.read_csv("data.csv")

#                   BELOW APPLY TO THE ALL DATAFRAME
# print(df.mean(numeric_only=True))   # allowing just average of numerical values
# No           75.500000
# Height        1.200000
# Weight       46.231333
# Legendary     0.026667
# dtype: float64

# print(df.sum(numeric_only=True))
# No           11325.0
# Height         180.0
# Weight        6934.7
# Legendary        4.0
# dtype: float64

# print(df.min(numeric_only=True))
# No           1.0
# Height       0.2
# Weight       0.1
# Legendary    0.0
# dtype: float64

# print(df.max(numeric_only=True))
# No           150.0
# Height         8.8
# Weight       460.0
# Legendary      1.0
# dtype: float64

# print(df.count())
# No           150
# Name         150
# Type1        150
# Type2         67  because not all pokemons has a type2
# Height       150
# Weight       150
# Legendary    150
# dtype: int64

#                   SINGLE COLUMN
print(df["Height"].mean()) # 1.2
print(df["Height"].sum()) # 180.0
print(df["Height"].min()) # 0.2
print(df["Height"].max()) # 8.8
print(df["Height"].count()) # 150
print(df["Type2"].count()) # 67

group = df.groupby("Type1")

print(group["Height"].mean())
# Type1
# Bug         0.900000
# Dragon      2.666667
# Electric    0.855556
# Fairy       0.950000
# Fighting    1.185714
# Fire        1.216667
# Ghost       1.466667
# Grass       1.083333
# Ground      0.850000
# Ice         1.550000
# Normal      0.986364
# Poison      1.221429
# Psychic     1.371429
# Rock        1.844444
# Water       1.300000
# Name: Height, dtype: float64

print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())