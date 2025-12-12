import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def generate_random_centroids(df, k):
    centroids = []
    for i in range(k):
        centroid = df.apply(lambda col : float(col.sample()))
        centroids.append(centroids)
    centroids_df = pd.concat(centroids, axis=1)
    return centroids_df

#def k_means_sklearn():
    

#def k_means():
