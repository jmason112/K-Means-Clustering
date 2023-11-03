#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the data from cybersecuritybreaches.csv into a data frame object
data = pd.read_csv('cybersecuritybreaches.csv')

# Remove the string columns from the data
data = data.select_dtypes(include=[np.number])

# Replace NaN values with 0
data = np.nan_to_num(data)

# Perform K-Means clustering on the data
kmeans = KMeans(n_init=20)
kmeans.fit(data)

# Calculate WCSS
wcss = kmeans.inertia_
print("WCSS:", wcss)

# Calculate silhouette score
silhouette_avg = silhouette_score(data, kmeans.labels_)
print("Silhouette Score:", silhouette_avg)

# Plot the data points and cluster centroids as scatter plot
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plt.show()

# Plot the WCSS and silhouette_score for different values of k
wcss_values = []
silhouette_scores = []
for k in range(2, 21):
    print("Running KMeans with k =", k)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data, kmeans.labels_))

plt.plot(range(2, 21), wcss_values)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

plt.plot(range(2, 21), silhouette_scores)
plt.title('Silhouette Method')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.show()
