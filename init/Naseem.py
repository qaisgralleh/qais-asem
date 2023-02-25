import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('kc_house_data.csv')
# Y price
# X -> bedrooms , bathrooms , sqft_living ,sqft_lot ,floors,waterfront
df = df[["price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront"]]
# df.info()
print(df[["sqft_living"]].describe())
# df['bedrooms'].hist()
# plt.show()
mixMAx = MinMaxScaler()

df['price'] = df[['price']] / 10000

beds = df['bedrooms'].values.reshape(-1, 1)
df['bedrooms'] = mixMAx.fit_transform(beds)

sqft_living = df['sqft_living'].values.reshape(-1, 1)
df['sqft_living'] = mixMAx.fit_transform(sqft_living)

sqft_lot = df['sqft_lot'].values.reshape(-1, 1)
df['sqft_lot'] = mixMAx.fit_transform(sqft_lot)


train, test = train_test_split(df, test_size=.15)
train = pd.DataFrame(train)

x_train = train.drop(columns=["price"], axis=1)
y_train = train["price"]
model = LinearRegression()
model.fit(x_train,y_train)
x_test = test.drop(columns=["price"], axis=1)
y_test = test["price"]


pred = model.predict(x_test[:5])
print(pred)
print(y_test[:5])
