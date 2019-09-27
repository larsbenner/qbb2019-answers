#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

af2 = []
for line in open(sys.argv[1]): #snpeff
   if line.startswith("#"):
       continue
   fields = line.rstrip("\t").split()
   allele_frequency = (fields[7])
   af1 = allele_frequency.split("=")[1]
   if "," in af1:
       af1 = float(af1.split(",")[0])  
   else:
       af1 = float(af1)
   af2.append(af1)
 
#print(af2)

fig, ax = plt.subplots()
ax.hist(af2, bins=100, density = True)
ax.set_xlabel("Allele")
ax.set_ylabel("Frequency")
ax.set_title("Allele Frequency Spectrum")
#ax.plot(x, y)
#fig.savefig("af.png")
fig.savefig("af.png")
plt.close(fig)
   
 
#column for familyID, modify family pheno in python and add
#fid in 1st and _id in 2nd  want values for each othe thos in first row
#iterate thru lines of file for each 
#modify file we hace to add individual and family Ids    
       
      