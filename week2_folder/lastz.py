#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


df1 = open(sys.argv[1])

#dic = {}

list_contigs = []
list_ref = []
  
for line in df1:
    if "#score" in line:
        continue
    column = line.rstrip('\r\n').split("\t")
    list_contigs.append(int(column[8]))
    list_ref.append(int(column[5])-int(column[4]))


# print (list_contigs)
# print (list_ref)
     
fig, ax = plt.subplots()
ax.scatter( list_contigs, list_ref )
ax.set_xlabel("length of contigs")
ax.set_ylabel("length of reference")
ax.set_title( "Length of reference vs. length of contigs" )
fig.savefig( "ref_contig_length.png" )
plt.close( fig )