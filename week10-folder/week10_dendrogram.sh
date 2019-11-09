#!/usr/bin/env python3
import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

hema_data = open(sys.argv[1])
# Z = linkage(input_file, 'ward')

df1 = pd.read_csv(hema_data, sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_")
print(df1)
genedf = df1.iloc[1:,:]
# print(genedf)
gene_list = df1.index.tolist()
# print(gene_list)
T_genedf = genedf.transpose()
celltype_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
celltype_list_1 = ["poly", "unk", "CFU", "mys", "int", "mid", "respectively"]
# print(genedf)
# print(T_genedf)
Z1 = linkage(genedf, 'average')
Z2 = linkage(T_genedf, 'average')
#print(Z1)
#print(Z2)



plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel(celltype_list_1)
plt.ylabel('distance')
dendrogram(
    Z2,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.savefig('dendrogram.png')
plt.show()