#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


df1 = open(sys.argv[1])
df2 = open(sys.argv[2])
df3 = open(sys.argv[3])
df4 = open(sys.argv[4])

dic = {}

for line in df1:
    column = line.rstrip('\r\n').split("\t")
    if column[0] == "t_id":
        continue
    dic[column[5]] = [column[11]]
    
for line in df2:
    column = line.rstrip('\r\n').split("\t")
    dic[column[0]].append(column[4])
    
for line in df3:
    column = line.rstrip('\r\n').split("\t")
    dic[column[0]].append(column[4])
    
for line in df4:
    column = line.rstrip('\r\n').split("\t")
    dic[column[0]].append(column[4])
    
#print (dic)


    
#H3K4me1
df = pd.DataFrame.from_dict(dic, orient='index')
df = df.replace(to_replace='None', value=np.nan).dropna()
df.columns = ['fpkm', 'h3k4me1','h3k4me3','h3k9me3']
#print(df)

y = df.iloc[:,0]
x = df.iloc[:,1]

result = sm.OLS(y.astype(float), x.astype(float)).fit()
print(result.params)
print(result.summary())


#H3K4me3
df = pd.DataFrame.from_dict(dic, orient='index')
df = df.replace(to_replace='None', value=np.nan).dropna()
df.columns = ['fpkm', 'h3k4me1','h3k4me3','h3k9me3']
#print(df)

y = df.iloc[:,0]
x = df.iloc[:,2]

result = sm.OLS(y.astype(float), x.astype(float)).fit()
print(result.params)
print(result.summary())

#H3K9me3
df = pd.DataFrame.from_dict(dic, orient='index')
df = df.replace(to_replace='None', value=np.nan).dropna()
df.columns = ['fpkm', 'h3k4me1','h3k4me3','h3k9me3']
#print(df)

y = df.iloc[:,0]
x = df.iloc[:,3]

result = sm.OLS(y.astype(float), x.astype(float)).fit()
print(result.params)
print(result.summary())








# #FBtr0302347
# #reads in our tab files with chromatin averages over promoter regions
# our_data = {}
# df = pd.read_csv(sys.argv[1], header=None,index_col=0,sep="\t")
# # df.columns = ["1","2","3",sys.argv[1],"5"]
# #our_data[sys.argv[1]] = df.iloc[:,11]
#
# print(df)
#
# new_file = pd.DataFrame(df.loc[:,[1][11]])
# # new_file.columns = ["FPKM"]
# # new_file["FPKM"] = pd.to_numeric(new_file["FPKM"])
# #
# # col_names = df.columns.values.tolist()
# #
# #
# # df = pd.DataFrame(our_data)
# #
# #
# # df = pd.read_csv(sys.argv[1], index_col = "t_name" )
# # col_names = df.columns.values.tolist()
# # print(col_names)
# # #Will print singlecolumn gene expression for gene neame 'FBr' for 2nd column
# # goi = pd.DataFrame( df.loc[sys.argv[2]].iloc[1:])
# # goi.columns = ["FPKM"]
# # goi["FPKM"] = pd.to_numeric(goi["FPKM"])
# # #break index column into sex and stage columns by splitting on first one
# # goi["sex"], goi["stage"] = goi.index.str.split("_", 1).strs