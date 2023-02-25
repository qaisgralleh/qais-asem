import pandas as pd
df = pd.read_csv("car data.csv")
print(df.loc[83 , "Year"])
df.loc[83 , "year"] =2015
print(df.loc[83 ,"Year"])

df["new"] = df["Year"] > 2015
print(df[["Year","new"]].head())
df ["valid"] = df["Year"] < 2023
print(df[["Year", "new" ,"valid"]].head())

