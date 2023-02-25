import pandas as pd

df = pd.read_csv('car data.csv')
df.info()
df["string" ] = df ["Selling_Price_2"].astype(str)
df.info
df["selling_price_2"]= df.df["string"].astype(float)

df["max"] = df["selling_price_2"] * 2
print(df.head())
df.info()