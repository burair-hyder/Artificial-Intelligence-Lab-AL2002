# LAB 10
# QUESTION 03
import kagglehub
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

path = kagglehub.dataset_download("shwetabh123/mall-customers")
df = pd.read_csv(os.path.join(path, "Mall_Customers.csv"))

df["customer_class"] = (df["Spending Score (1-100)"] >= 50).astype(int)

X = df[["Age", "Annual Income (k$)"]]
y = df["customer_class"]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

new_customer = pd.DataFrame({
    "Age": [30],
    "Annual Income (k$)": [60]
})

result = model.predict(new_customer)
print("Customer Class:", result[0])
print("0 = Low Spending Customer, 1 = High Spending Customer")
