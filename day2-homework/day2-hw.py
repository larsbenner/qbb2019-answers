#!/usr/bin/env python3

import sys
import numpy

"""Print all unique gene names from a t_data.ctab file"""

f = sys.argv[1]

fly_base = []
ac_uniprot = []
for line in open(f):
    if "DROME" and "FBgn" in line:
        fields = line.split()
        fly_base = fields[-1]
        ac_uniprot = fields[-2]
        print (fly_base, "\t", ac_uniprot)
    else:
        continue
        
        
        
        
        
        
        
        


    