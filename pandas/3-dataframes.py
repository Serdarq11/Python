import pandas as pd

# Dataframe: A tabular data structure with rows AND columns. (2-dimensional)
#            Similar to an excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)
#                  Name  Age
# Employee 1  Spongebob   30
# Employee 2    Patrick   35
# Employee 3  Squidward   50

print(df.loc["Employee 1"])
# Name    Spongebob
# Age            30
# Name: Employee 1, dtype: object

# add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

print(df)
#                  Name  Age      Job
# Employee 1  Spongebob   30     Cook
# Employee 2    Patrick   35      N/A
# Employee 3  Squidward   50  Cashier

# add a new row
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                         index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])

print(df)
#                  Name  Age       Job
# Employee 1  Spongebob   30      Cook
# Employee 2    Patrick   35       N/A
# Employee 3  Squidward   50   Cashier
# Employee 4      Sandy   28  Engineer
# Employee 5     Eugene   60   Manager

