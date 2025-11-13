import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("data.csv", index_col="Name")  # index_col="Name" makes the first column -> Name of the pokemons

#SELECTION BY COLUMN

#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df["Weight"].to_string())

# SELECTING MULTIPLE COLUMNS
#print(df[["Name", "Height", "Weight"]].to_string())


# SELECTION BY ROW/S
print(df.loc["Pikachu", ["Height", "Weight"]])
# Height    0.4
# Weight    6.0
# Name: Pikachu, dtype: object

print(df.loc["Charizard" : "Blastoise", ["Height", "Weight"]])  # gave me every pokemon from Charizard to Blastoise
#            Height  Weight
# Name                     
# Charizard     1.7    90.5
# Squirtle      0.5     9.0
# Wartortle     1.0    22.5
# Blastoise     1.6    85.5

print(df.iloc[0:11])    # 11 is exclusive, so it will give me first 10 rows
print(df.iloc[0:11:2])    # gives me every second row
print(df.iloc[0:11:2, 0:3])    # gives me every second row and first 3 columns

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found!")