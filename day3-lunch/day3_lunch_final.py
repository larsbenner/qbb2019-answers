#!/usr/bin/env python3

import sys

"""parses txt file to chromosome 3"""

f = sys.argv[1]
"""parses 3R CDS files into just gene ranges and gene IDs"""

gene_list = []
for line in open(f):
    fields = line.split("\t")
    """iterates through file"""
    if fields[0] == "3R":
        if 'gene_biotype "protein_coding"' in fields[8]:
            if fields[2] == "gene":
                gene_start = int(fields[3])
                gene_end = int(fields[4])
                gene_id = fields[8]
                gene_list.append((gene_start, gene_end, gene_id))

lo = 0
hi = len(gene_list) - 1
mid = 0
number_int = 0
search_pos = 21378950

while lo < hi:
    number_int +=1
    mid = int((hi+lo)/2)
    if (search_pos < gene_list[mid][0]):
        hi = mid
    elif search_pos > gene_list[mid][1]:
        lo = mid + 1
    else:
        break
        
print(gene_list[lo], number_int)

