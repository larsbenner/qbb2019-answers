#!/usr/bin/env python3

import sys
import scanpy as sc
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")

adata.var_names_make_unique()

# #
# sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
# sc.tl.pca(adata)
#
# sc.pp.neighbors(adata)
# sc.tl.louvain(adata, resolution=0.3)
#
# fig, ax = plt.subplots()
#
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color=['louvain'], ax=ax, show=False)
#
# #sc.tl.umap(adata)
# #sc.pl.umap(adata, color=['louvain'], ax=ax, show=False)
#
# plt.show()
#
# #
sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.louvain(adata, resolution=0.3)

# fig, ax = plt.subplots()
#
# sc.tl.rank_genes_groups(adata, groupby='louvain', method='t-test')
# sc.pl.rank_genes_groups(adata, groupby='louvain', method='t-test', show=False)
#
# plt.show()

fig, ax = plt.subplots()

sc.tl.rank_genes_groups(adata, groupby='louvain', method='logreg')
sc.pl.rank_genes_groups(adata, groupby='louvain', method='logreg', show=False)

plt.show()
