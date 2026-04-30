# TASK 2 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


path = house_prices_advanced_regression_techniques_path

df = pd.read_csv(os.path.join(path, "train.csv"))

print(df.shape)
print(df.head())


for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())


df = pd.get_dummies(df, drop_first=True)


X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


lr = LinearRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)


dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
pred_dt = dt.predict(X_test)


mae_lr = mean_absolute_error(y_test, pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, pred_lr))

mae_dt = mean_absolute_error(y_test, pred_dt)
rmse_dt = np.sqrt(mean_squared_error(y_test, pred_dt))


print("\nLinear Regression")
print("MAE:", mae_lr)
print("RMSE:", rmse_lr)

print("\nDecision Tree")
print("MAE:", mae_dt)
print("RMSE:", rmse_dt)


if rmse_lr < rmse_dt:
    print("\nBest Model: Linear Regression")
else:
    print("\nBest Model: Decision Tree")


comparison = pd.DataFrame({
    "Actual": y_test.values,
    "LR_Pred": pred_lr,
    "DT_Pred": pred_dt
})

print("\nSample Comparison:")
print(comparison.head(10))


plt.scatter(y_test, pred_lr)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Linear Regression: Actual vs Predicted")
plt.show()
