import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("data.csv")

# Filtering: Keeping the rows that match a condition

# tall_pokemon = df[df["Height"] >= 2]

# heavy_pokemon = df[df["Weight"] > 100]

# legendary_pokemon = df[df["Legendary"] == 1]    # or typing True instead of 1

# water_pokemon = df[(df["Type1"] == "Water") | 
#                    (df["Type2"] == "Water")
# ]

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]  # ff -> fire flying

print(ff_pokemon)

