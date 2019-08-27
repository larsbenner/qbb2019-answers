#!/usr/bin/env python3

import sys
import numpy

"""parses txt file to get FLYbase ID and uniprot ID"""

f = sys.argv[1]

fly_base = []
ac_uniprot = []
for line in open(f):
    """iterates through file"""
    if "DROME" and "FBgn" in line:
        fields = line.split()
        fly_base = fields[-1]
        ac_uniprot = fields[-2]
        """prints parsed file"""
        print (fly_base, "\t", ac_uniprot)
    else:
        continue
        
        
        
        
        
        
        
        


    