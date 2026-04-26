# LAB 11 
# QUESTION 02
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

X = df.drop("vehicle_serial_no", axis=1)
X = pd.get_dummies(X, columns=["vehicle_type"], drop_first=True)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method (No Scaling)")
plt.show()

kmeans1 = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster_No_Scaling"] = kmeans1.fit_predict(X)

scaler = StandardScaler()
cols = [col for col in X.columns if "vehicle_type" not in col]
X_scaled = X.copy()
X_scaled[cols] = scaler.fit_transform(X_scaled[cols])

kmeans2 = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster_With_Scaling"] = kmeans2.fit_predict(X_scaled)

print(df[["Cluster_No_Scaling"]].value_counts())
print(df[["Cluster_With_Scaling"]].value_counts())

plt.scatter(df["mileage"], df["fuel_efficiency"], c=df["Cluster_With_Scaling"])
plt.xlabel("Mileage")
plt.ylabel("Fuel Efficiency")
plt.title("Clusters (With Scaling)")
plt.show()
