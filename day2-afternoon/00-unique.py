#!/usr/bin/env python3

"""Print all unique gene names from a t_data.ctab file"""

import sys

#gene_names_seen = []
#gene_names_seen = {}
gene_names_seen = set()

for i, line in enumerate( sys.stdin ):
    #ignore header on first line
    if i == 0:
        continue
    #gene name in 9th field
    fields = line.rstrip("\n").split("\t")
    gene_name = fields[9]
    #add only of not there before
    if gene_name in gene_names_seen:
        continue
    else:
        #gene_names_seen.append( gene_name )
        gene_names_seen.add()

for name in gene_names_seen:
    print(name)
    
        



