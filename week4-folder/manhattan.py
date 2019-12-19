#!/usr/bin/env python3
import sys
import os
import numpy as np
import matplotlib.pyplot as plt


chrom_tup=[]
chr_length = {}
cc_dict = {}
chr_list = []


for file_name in os.listdir(os.getcwd()):
    if file_name.endswith(".qassoc"):
       q_assoc_file = open(file_name)
       for i, line in enumerate(q_assoc_file):
           if i == 0:
               continue
           if "NA" in line:
               continue
           p_value = float(line.rstrip().split()[-1])
           chrom = line.rstrip().split()[0]
           #chr_list.add(chrom)
           #position = line.rstrip().split()[2]
           chrom_tup.append((chrom, -np.log10(p_value)))
           if chrom not in chr_list:
               chr_list.append(chrom)
               
           #chr_length[chrom]= position
           
    chr_color = list(chr_list)
    colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']       
    for i in range(len(chr_color)):
        cc_dict[chr_color[i]] = colors[i]
    start_point = 1
             #offset = 0
    fig, ax = plt.subplots()
    for chr in chr_color:
        for point in chrom_tup:
            if point[0] == chr:
                ax.scatter(start_point, point[1], color = cc_dict[point[0]], s = 2)
                if point[1] > 5:
                    ax.scatter(start_point, point[1], color = "red", s = 2)    
                start_point += 1
             # elif point[0] != chr:
   #                 offset = chr_length[chr]
    plt.tight_layout()
    fig.savefig("MAplot.png")
    plt.close(fig)
    break



           
           
           
           
#print(chrom_tup)
#print(dict)



        
    

#print(family_id)
#print(individual_id)

#output list of strings in python separt
    