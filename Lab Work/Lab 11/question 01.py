# LAB 11 
# QUESTION 01 

import kagglehub
import pandas as pd
import os

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("shwetabh123/mall-customers")

print("Dataset path:", path)
print("Files:", os.listdir(path))

csv_file = os.listdir(path)[0]
df = pd.read_csv(os.path.join(path, csv_file))

print(df.head())
print(df.columns)

customer_id_col = None

for col in df.columns:
    if "id" in col.lower():
        customer_id_col = col
        break

if customer_id_col:
    X = df.drop(customer_id_col, axis=1)
else:
    X = df.copy()

X = pd.get_dummies(X, drop_first=True)

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method Without Scaling")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans_no_scaling = KMeans(n_clusters=5, random_state=42, n_init=10)
clusters_no_scaling = kmeans_no_scaling.fit_predict(X)

df["Cluster_Without_Scaling"] = clusters_no_scaling

X_scaled = X.copy()

cols_to_scale = []

for col in X_scaled.columns:
    if col.lower() != "age":
        cols_to_scale.append(col)

scaler = StandardScaler()
X_scaled[cols_to_scale] = scaler.fit_transform(X_scaled[cols_to_scale])

kmeans_with_scaling = KMeans(n_clusters=5, random_state=42, n_init=10)
clusters_with_scaling = kmeans_with_scaling.fit_predict(X_scaled)

df["Cluster_With_Scaling"] = clusters_with_scaling

print("\nCluster Counts Without Scaling:")
print(df["Cluster_Without_Scaling"].value_counts())

print("\nCluster Counts With Scaling:")
print(df["Cluster_With_Scaling"].value_counts())

print("\nFinal Dataset:")
print(df.head())

income_col = None
score_col = None

for col in df.columns:
    if "income" in col.lower():
        income_col = col
    if "score" in col.lower():
        score_col = col

if income_col and score_col:
    plt.scatter(df[income_col], df[score_col], c=df["Cluster_With_Scaling"])
    plt.title("Customer Clusters With Scaling")
    plt.xlabel(income_col)
    plt.ylabel(score_col)
    plt.show()
else:
    print("Income and spending score columns were not found for plotting.")
