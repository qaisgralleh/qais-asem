import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('car data.csv')
df.info()
print(df.describe())

#print(df.head())
df["Selling_Price"].plot()
df["Year"].hist()
df.plot.scatter(x="Year", y="Selling_Price")
plt.show()
#selling_price