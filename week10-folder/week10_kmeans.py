#!/usr/bin/env python3
import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


hema_data = open(sys.argv[1])

df1 = pd.read_csv(hema_data, sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_", skiprows=[0])
#print(df1)
x = df1["cfu"].values
#print(x)
y = df1["poly"].values
#print(y)

df = DataFrame({"cfu": x, "poly": y})
print(df)
  
kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['cfu'], df['poly'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.title('K-means clustering graph')
plt.savefig('kmeans.png')
plt.show()

# genedf = df1.iloc[1:,:]
# # print(genedf)
# gene_list = df1.index.tolist()
# # print(gene_list)
# T_genedf = genedf.transpose()
# celltype_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
# # print(genedf)
# # print(T_genedf)
# Z1 = linkage(genedf, 'average')
# Z2 = linkage(T_genedf, 'average')
# #print(Z1)
# #print(Z2)
# k1 = leaves_list(Z1)
# k2 = leaves_list(Z2)
# #print(k2)
#
# genedfx = float(genedf.loc[1])
# genedfy = float(genedf_1.loc[2])
# print(genedfx)
# print(genedfy)