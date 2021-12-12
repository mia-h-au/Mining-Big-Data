import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

data = pd.read_csv("iris.txt", header = None)

label = data.loc[:,4]
data = data.loc[:,range(4)]

reducer = PCA(n_components=2)
reduced_data = reducer.fit_transform(data)

km = KMeans(n_clusters=5)

cluster = km.fit(reduced_data)

plt.scatter(reduced_data[:, 0], reduced_data[:, 1], label='Datapoints')
plt.scatter(cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1], label='Clusters')
plt.title("KMeans on Iris dataset")
plt.legend()
plt.show()