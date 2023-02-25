import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("diabetes.csv")
df.loc[df["BloodPressure"] == 0 , "BloodPressure" ]= 72
train ,test = train_test_split(df , test_size= 0.2)

train = pd.DataFrame(train)
X_train = train.drop(columns=["Outcome"] , axis=1)
Y_train = train["Outcome"]

model = LogisticRegression(max_iter=10000)
model.fit(X_train , Y_train)
test = pd.DataFrame(test)
X_test = train.drop(columns=["Outcome"] , axis=1)
Y_test = train["Outcome"]
pred = model.predict(X_test)
#print(pred)
#print(Y_test[:5])
print(accuracy_score(Y_test ,pred))



