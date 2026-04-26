# LAB 10
# QUESTION 01
import kagglehub
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

path = kagglehub.dataset_download("camnugent/california-housing-prices")

print("Dataset Path:", path)
print("Files:", os.listdir(path))

df = pd.read_csv(os.path.join(path, "housing.csv"))

print(df.head())

df = df.dropna()

df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)

X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

pred = model.predict(x_test)

mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
