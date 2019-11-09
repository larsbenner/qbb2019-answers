#!/usr/bin/env python3
import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
import pandas as pd
import seaborn as sns


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
# print(genedf)
# print(T_genedf)
Z1 = linkage(genedf, 'average')
Z2 = linkage(T_genedf, 'average')
#print(Z1)
#print(Z2)
k1 = leaves_list(Z1)
k2 = leaves_list(Z2)
#print(k2)

genedf_1 = genedf.iloc[k1,:]
genedf2 = genedf_1.iloc[:,k2]
print(genedf2)

FPKM_matrix = genedf2.values.astype(float)

fig, ax = plt.subplots()
im = ax.imshow(FPKM_matrix, aspect = "auto")
ax.set_xlabel("cell_type")
ax.set_ylabel("gene")
ax.set_title("Heatmap of Cell Types")
fig.colorbar(im, ax = ax)
plt.savefig('heatmap.png')
plt.show()
plt.close()

# # create some random data; replace that by your actual dataset
# data = pd.DataFrame(np.random.rand(14, 0), columns=['poly', 'unk', 'C', 'D', 'int', 'mid'], index = range(0, 14, 1))
#
# # plot heatmap
# ax = sns.heatmap(data.T)
#
# # turn the axis label
# for item in ax.get_yticklabels():
#     item.set_rotation(0)
#
# for item in ax.get_xticklabels():
#     item.set_rotation(90)
#
# # save figure
# plt.savefig('seabornPandas.png', dpi=100)
# plt.show()
# plt.title('Hierarchical Clustering Dendrogram (truncated)')
# plt.xlabel('sample index')
# plt.ylabel('distance')
# dendrogram(
#     df1,
#     truncate_mode='lastp',  # show only the last p merged clusters
#     p=6,  # show only the last p merged clusters
#     show_leaf_counts=False,  # otherwise numbers in brackets are counts
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,  # to get a distribution impression in truncated branches
# )
# plt.show()

