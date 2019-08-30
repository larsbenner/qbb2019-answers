#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#FBtr0302347
#reads in our tab files with chromatin averages over promoter regions
our_data = {}
df = pd.read_csv(sys.argv[1], header=None,index_col=0,sep="\t")
# df.columns = ["1","2","3",sys.argv[1],"5"]
our_data[sys.argv[1]] = df.iloc[:,3]

print(df)
print()

col_names = df.columns.values.tolist()


df = pd.DataFrame(our_data)


df = pd.read_csv(sys.argv[1], index_col = "t_name" )
col_names = df.columns.values.tolist()
#Will print single column gene expression for gene neame 'FBr' for 2nd column
goi = pd.DataFrame( df.loc[sys.argv[2]].iloc[1:])
goi.columns = ["FPKM"]
goi["FPKM"] = pd.to_numeric(goi["FPKM"])
#break index column into sex and stage columns by splitting on first one
goi["sex"], goi["stage"] = goi.index.str.split("_", 1).strs