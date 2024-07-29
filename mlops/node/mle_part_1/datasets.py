from sklearn import datasets
import pandas as pd

X, y = datasets.fetch_california_housing(return_X_y=True, as_frame=True)
df = pd.concat([X, y], axis="columns")
print(df.head())
print(df.dtypes)