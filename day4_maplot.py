#!/usr/bin/env python3

"""usage: <ctab1><ctab2> """

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


#specify row names with index column t_name to makes ure ur comparing same tx
#split string in sys.argv1 -2 is directory name
#purpose of os?
#indexes columns based on name so each transcript is lined up
name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" ) 


# fpkm = {"sample1" : [1,2,3],
# "sample2": [4,5,6]}
#name1 becomes new col name
fpkm = {name1: ctab1.loc[:,"FPKM"],
        name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)

M = np.log2(df["SRR072903"]+1) - np.log2(df["SRR072904"]+1)
A = (np.log2(df["SRR072903"] + 1) + np.log2(df["SRR072904"]+1)) * .5

fig, ax = plt.subplots()
ax.scatter( A, M )
# ax.plot( [0, 10], [-2, 2] )
fig.suptitle("MA plot for SRR072903 vs. SRR072904 samples")
ax.set_xlabel("mean read count")
ax.set_ylabel("log2 fold change")
fig.savefig( "MA_plot.png" )
plt.close( fig ) 



# print(df)
# print(type(df))