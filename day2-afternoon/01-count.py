#!/usr/bin/env python3

"""Count transcripts per gene from a t_data.ctab file"""

import sys

gene_name_count = {}

for i, line in enumerate( sys.stdin ):
    #ignore header on first line
    if i == 0:
        continue
    #gene name in 9th field
    fields = line.rstrip("\n").split("\t")
    gene_name = fields[9]
    #add only of not there before
    if gene_name in gene_name_count:
        gene_name_count[gene_name] += 1
    else:
        gene_name_count[gene_name] = 1

for name in gene_name_count:
    print(name, gene_name_count[name])
    
        



