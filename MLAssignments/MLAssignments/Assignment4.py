
import numpy as np
import pandas as pd
import matplotlib as mp
dataframe= pd.read_csv('Categorical.csv')
newdf = dataframe['continent'].map({'North America':0,'Europe':1,'Asia':2,'Africa':3,'South America':4, 'Oceania':5,'Seven seas (open ocean)':6, 'Antarctica':7})
print(newdf)
feature = dataframe.loc[:,"continent"]


k = 4
clusters = {}
centroids = {}
for i in range(k):
    clusters[i] = []

print(clusters)

for i in range(k):
    centroids[i] = newdf[i]

print(centroids)

for data in newdf:
    euc_dist = []
    for j in range(k):
        # print(data)
        # print(centroids[j])
        euc_dist.append(np.linalg.norm(data - centroids[j]))
    clusters[euc_dist.index(min(euc_dist))].append(data)

print(clusters)

def recalculate_clusters(X, centroids, k):
    """ Recalculates the clusters """
    # Initiate empty clusters
    clusters = {}
    # Set the range for value of k (number of centroids)
    for i in range(k):
        clusters[i] = X[i]
    for data in X:
        euc_dist = []
        for j in range(k):
            euc_dist.append(np.linalg.norm(data - centroids[j]))
            print(euc_dist)
        # Append the cluster of data to the dictionary
        clusters[euc_dist.index(min(euc_dist))].append(data)

    return clusters
def recalculate_centroids(centroids, clusters, k):
    """ Recalculates the centroid position based on the plot """
    for i in range(k):
        centroids[i] = np.average(clusters[i], axis=0)
    return centroids

# recalculate_clusters(newdf, centroids, k )
recalculate_centroids(centroids, clusters, k)