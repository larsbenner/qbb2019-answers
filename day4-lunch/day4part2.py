#!/usr/bin/env python3

"""usage: <ctab1><ctab2> """

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from numpy.polynomial.polynomial import polyfit

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


A = np.log2(df.iloc[:,0]+1)
B = np.log2(df.iloc[:,1]+1)
#
fig, ax = plt.subplots()
ax.scatter(A, B, color='blue', alpha=.1 )

z=np.polyfit(A, B, 3)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(0,10 , 50)
y_new = f(x_new)


plt.plot(A[0],A[-1], x_new, y_new)

fig.suptitle("FPKM Comparisons")
ax.set_xlabel("Sample A log2 FPKM Values")
ax.set_ylabel("Sample B log2 FPKM Values")
fig.savefig( "FinalScatter1.png" )
plt.close( fig )