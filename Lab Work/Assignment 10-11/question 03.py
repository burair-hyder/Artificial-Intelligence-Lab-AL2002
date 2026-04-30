# TASK 3
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("marketing_campaign.csv", sep="\t")

print(df.shape)
print(df.head())


df = df.dropna()


features = [
    "Income",
    "Recency",
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

X = df[features]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


wcss = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)


plt.plot(range(2, 11), wcss, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()


kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)


df["Cluster"] = clusters


plt.scatter(df["Income"], df["MntWines"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.title("Customer Segmentation")
plt.show()


print(df[["Income", "MntWines", "Cluster"]].head(20))
