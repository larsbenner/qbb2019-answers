#!/usr/bin/env python3

"""Count transcripts of selected genes from a t_data.ctab file"""

"""usage ./02-count-goi.py ,gene name file. , ,gtf."""

import sys

genes_of_interest = set()
for line in open ( sys.argv[1] ):
    genes_of_interest.add( line.strip())
    
gene_name_count = {}

for i, line in enumerate( sys.stdin ):
    #Ignore header on first line

    if i == 0:
        continue
    #get the gene name
    fields = line.rstrip("\n").split("\t")
    gene_name = fields[9]
    #add gene if not seen before
    if gene_name not in genes_of_interest:
        continue
    
    if gene_name in gene_name_count:
        gene_name_count[gene_name] += 1
    else:
        gene_name_count[gene_name] = 1

for name in gene_name_count:
    print(name, gene_name_count[name])
    
        



