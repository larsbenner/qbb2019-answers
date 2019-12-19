#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

pca_1 = []
pca_2 = []

for line in open(sys.argv[1]): #snpeff
   fields = line.rstrip("\t").split()
   pca_1.append(float(fields[2]))
   pca_2.append(float(fields[3]))

# print(pca_1)
# print(pca_2)

fig, ax = plt.subplots()
ax.scatter( pca_1, pca_2 )
ax.set_xlabel("pca_1")
ax.set_ylabel("pca_2")
ax.set_title ("PCA Plot")
fig.savefig( "pca.png" )
plt.close( fig )


