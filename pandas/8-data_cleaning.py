import pandas as pd

# Data cleaning: The process of fixing/removing
#                incomplete, incorrect or irrevelant data
#                ~75% of work done with Pandas is data cleaning

df = pd.read_csv("data.csv")

# 1.Drop irrevelant columns
#df = df.drop(columns=["Legendary", "No"])


# 2.Handle missing data
# df = df.dropna(subset=["Type2"])    # dropna = Drop Not Available, we removed rows that are missing Type2 value
df = df.fillna({"Type2": "None"})     # instead of NaN, we see None in Type2 that has not value 



# 3.Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                  "Fire": "FIRE",
                                  "Water": "WATER"})



# 4.Standardize text
df["Name"] = df["Name"].str.lower()


# 5.Fix data types
df["Legendary"] = df["Legendary"].astype(bool)  # replaced 0 and 1 with True and False


# 6.Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())

