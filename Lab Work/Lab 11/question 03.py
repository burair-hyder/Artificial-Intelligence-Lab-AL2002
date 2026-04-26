# LAB 11 
# QUESTION 03

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    "student_id": [1,2,3,4,5,6,7,8,9,10],
    "GPA": [3.5, 2.8, 3.9, 2.5, 3.2, 3.8, 2.7, 3.0, 3.6, 2.9],
    "study_hours": [15, 8, 20, 5, 12, 18, 7, 10, 16, 9],
    "attendance_rate": [90, 70, 95, 60, 85, 92, 65, 75, 88, 72]
}

df = pd.DataFrame(data)

X = df[["GPA", "study_hours", "attendance_rate"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2,7), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

print(df)

plt.scatter(df["study_hours"], df["GPA"], c=df["Cluster"])
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.title("Student Clusters")
plt.show()
