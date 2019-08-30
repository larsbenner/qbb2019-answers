#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#df = pd.read_ctab(sys.argv[1], index_col = "t_name" )

# pomoter_right = []
# promoter_left =[]
for i, line in enumerate(open(sys.argv[1]) ):
    # Ignore header on first line
    if i == 0:
        continue
    # Get the gene name
    fields = line.rstrip("\n").split("\t")
    
    if fields[2] == "+":
        promter_left =  int(fields[3])-500
        promoter_right = int(fields[3])+500
    else:
        fields[2] == "-"
        promoter_left = int(fields[4]) +500
        promoter_right = int(fields[4]) - 500
        print(fields[1], promoter_left, promoter_right,fields[5], sep="\t")
        
        
         