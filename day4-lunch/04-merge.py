#!/usr/bin/env python3

 
"""usage: <ctab1><ctab2> """

import sys
import pandas as pd
import os

#specify row names with index column t_name to makes ure ur comparing same tx
#split string in sys.argv1 -2 is directory name
#purpose of os?
name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name" ) 


# fpkm = {"sample1" : [1,2,3],
# "sample2": [4,5,6]}

fpkm = {name1: ctab1.loc[:,"FPKM"],
name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)

print(df)
print(type(df))