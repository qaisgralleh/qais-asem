import pandas as pd
df = pd.read_csv('car data.csv')
print(df[["Year","kms_Driven","Fule_Type"]]).head()