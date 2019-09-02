#!/usr/bin/env python3


"""usage: 01-hist.py ctab
make histogram with FPKM"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
#import scipy.stats import skewnorm

fpkms = []
for i, line in enumerate( open(sys.argv[1])):
    if i ==0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]))
#print(len(fpkms))
#take log of data since have extreme values
my_data = np.log2(fpkms)

#paramters for a distributiion need mu and sigma
a = float(sys.argv[2])
mu = float(sys.argv[3])
sigma = float(sys.argv[4])
#gets x values
x = np.linspace(-15,15, 100)
#gets y values
y = stats.norm.pdf( x, mu, sigma ) 
y_skew = stats.skewnorm.pdf(x, a, loc=mu, scale=sigma )



#print(x)
#print(type(x))

#skewnorm distribution
#skewnorm.pdf()
    
#fig corresponds to entire figure and x corresponds to panel   
fig, ax = plt.subplots()
#using hist function in this line
#modifying hist to density = true ?
ax.hist(my_data, bins = 100, density=True)
#adds nother graph to overlay
ax.plot( x, y)
plt.plot(x,y_skew)

plt.xlabel("log2 fpkms")
plt.ylabel("Frequency")
plt.title("Histogram of log2fpkms")
plt.text(-15,.2, 'Sigma = %s\n a = %s\n Mu= %s' % (sigma, a, mu))
plt.plot(x, y_skew, color='orange', label='skewed distribution')
plt.plot(x, y, color='green', label='normaldistribution')
plt.legend(loc='upper left')

fig.savefig("fpkms.png")
plt.close(fig)


