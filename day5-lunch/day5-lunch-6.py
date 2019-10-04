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

df = pd.DataFrame.from_dict(dic, orient='index')
df = df.replace(to_replace='None', value=np.nan).dropna()
df.columns = ['fpkm', 'h3k4me1','h3k4me3','h3k9me3']
df['log2fpkm'] = np.log(df.iloc[:,0].astype(float) + 1)
#H3k4me1 log transformed fpkms 
x = df.iloc[:,4]
y = df.iloc[:,1]
result = sm.OLS(x.astype(float), y.astype(float)).fit()
predict = result.predict(x.astype(float))
print("h3k4me1_logtransformed")
print(result.summary())
print()

#H3k4me3 log transformed fpkms 
x = df.iloc[:,4]
y1 = df.iloc[:,2]
result1 = sm.OLS(x.astype(float), y1.astype(float)).fit()
predict1 = result1.predict(x.astype(float))
print("h3k4me3_logtransformed")
print(result.summary())
print()

x = df.iloc[:,4]
y2 = df.iloc[:,3]
result2 = sm.OLS(x.astype(float), y2.astype(float)).fit()
predict2 = result2.predict(x.astype(float))
print("h3k9me3_logtransformed")
print(result.summary())
print()


fig, (ax1,ax2,ax3) = plt.subplots(ncols=3)
ax1.hist( predict - x.astype(float), bins=1000, range=[-10, 10] )
ax2.hist( predict1 - x.astype(float), bins=1000, range=[-10, 10] )
ax3.hist( predict2 - x.astype(float), bins=1000, range=[-10, 10] )
ax1.set_xlabel("Log2 Reisidual FPKMs")
ax1.set_ylabel("Frequency")
ax2.set_xlabel("Log2 Reisidual FPKMs")
ax3.set_xlabel("Log2 Reisidual FPKMs")
ax1.set_title("H3K4me1")
ax2.set_title("H3K4me3")
ax3.set_title("H3K9me3")
ax1.set_ylim((0,90))
ax2.set_ylim((0,90))
ax3.set_ylim((0,90))
fig.savefig( "fpkms_logtransformed.png" )
plt.close(fig)