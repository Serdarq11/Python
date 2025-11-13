import pandas as pd

# Series: A pandas one-dimensional labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet (1-dimensional)

data = [100, 102, 104]  # if we put strings here, data type will be object, if boolean -> bool; and if float -> float
series = pd.Series(data, index=['a', 'b', 'c'])     # by default, indexes are 0, 1, 2, but we can change it to a, b, c

print(series)
# a    100
# b    102
# c    104
# dtype: int64

series.loc["c"] = 200   # reassignment

print(series.loc['a'])   # 100      # location by label -> loc
print(series.loc['b'])   # 102
print(series.loc['c'])   # 200

print(series.iloc[2])    # 200      # location by integer -> iloc


data2 = [100, 102, 104, 200, 202]
series = pd.Series(data2, index=["a", "b", "c", "d", "e"]) 

print(series)

print(series[series >= 200])
# d    200
# e    202
# dtype: int64

# dictionary
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series(calories)    # since dictionaries have already key values, we mustn't put index after calories

print(series)
# Day 1    1750
# Day 2    2100
# Day 3    1700
# dtype: int64

print(series.loc["Day 1"])  # 1750


series.loc["Day 3"] += 500

print(series.loc["Day 3"])  # 2200

print(series[series >=2000])
# Day 2    2100
# Day 3    2200
# dtype: int64
