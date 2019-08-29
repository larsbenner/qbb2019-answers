#!/usr/bin/env python3

"""usage: <ctab1><ctab2> """

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

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

print(df)
print(type(df))

fig,ax = plt.subplots()
ax.plot(float(df.loc[:,1]),float(df.loc[:,1]), color="red" )
fig.savefig("FPKM Comparison")
plt.close(fig)

#DataFrame.plot.scatter(x,y)

# fig,ax = plt.subplots()
# ax.scatter()
#
# ax.plot([0,40], [0,20000], color="red" )
# fig.savefig("comparison of transcripts")
# plt.close(fig)
