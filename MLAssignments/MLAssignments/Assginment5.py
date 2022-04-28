import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

df = pd.read_csv("Country-data.csv")

#for the column 'child_mort' and 'export'
data = df.iloc[:,[2,3]].values

clustering = DBSCAN(eps=2,min_samples=5).fit(data)

label = clustering.labels_

print(label)

#Calculating the number of clusters

clusters=len(set(label))- (1 if -1 in label else 0)
print('Total cluster:',clusters)

y_means = clustering.fit_predict(data)

plt.scatter(data[y_means == 0, 0], data[y_means == 0, 1], s = 50, c = 'red')
plt.scatter(data[y_means == 1, 0], data[y_means == 1, 1], s = 50, c = 'yellow')
plt.scatter(data[y_means == 2, 0], data[y_means == 2, 1], s = 50, c = 'blue')
plt.scatter(data[y_means == 3, 0], data[y_means == 3, 1], s = 50, c = 'green')
plt.scatter(data[y_means == 4, 0], data[y_means == 4, 1], s = 50, c = 'purple')
plt.scatter(data[y_means == 5, 0], data[y_means == 5, 1], s = 50, c = 'brown')
plt.xlabel('Export')
plt.ylabel('Health')

plt.title('Clusters')
plt.show()