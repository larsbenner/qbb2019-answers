#!/usr/bin/env python3
## this is for graphing motifs in binding sites

import sys
import matplotlib.pyplot as plt
import seaborn as sb

motif = open(sys.argv[1]) #motif file
binding_site = open(sys.argv[2]) #ER4sorted.txt #binding sites

motif_start_dict= {}

for line in motif:
    if line.startswith("#"):
        continue
    binding_site_sample = int(line.rstrip("/n").split()[0])
    strand = line.rstrip("\n").split()[6]
    #print (strand)
    motif_start = int(line.split()[3])
    motif_end = int(line.split()[4]) -1
    #print(strand, motif_start, motif_end)

    if strand == "+" in line:
        motif_start= motif_start

    if strand == "-" in line:
        motif_start = motif_end
    
    motif_start_dict.setdefault(binding_site_sample, [])
    motif_start_dict[binding_site_sample].append(motif_start)
    
#print(motif_start_dict)

locations= []
    #print (motif_start)
for i,line in enumerate(binding_site, 1):
    sample = i
    binding_start = int(line.split()[1])
    binding_stop = int(line.split()[2])
    length = binding_stop - binding_start
    for motif_start in motif_start_dict[sample]:
        rel_loc = motif_start/length
        locations.append(rel_loc)
        
fig, ax = plt.subplots()
sb.distplot(locations,bins=20, ax=ax)

ax.set_xlabel("Relative location of motif within binding site")
ax.set_ylabel("amount")
ax.set_title("Histogram")
fig.savefig("hist.png")
plt.close(fig)
#print(locations)
    