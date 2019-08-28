#!/usr/bin/env python3

import sys

"""takes in parsed data to see if it mathces ctab file"""

new_dict = {}
for line in open("final_parsed_file.txt"):
    columns = line.rstrip("\n").split("\t")
    list_genes_flybase = columns[0].strip()
    list_uniprot = columns[1].strip()
    new_dict[list_genes_flybase] = list_uniprot
    
"""enumerate through ctba file and takes gene identifier and see if it matches to parsed file"""
for i, line in enumerate(open("../results/stringtie/SRR072893/t_data.ctab")):
    if i == 0:
        continue
    new_col = line.rstrip("\n").split("\t")
    identifier = new_col[8]
    
    if identifier in new_dict:
         new_dict[identifier] = list_uniprot
         print(line.strip("\n"), identifier)
    elif identifier not in new_dict and sys.argv[1] == "nothing":
        continue
    elif identifier not in new_dict and sys.argv[1] == "default":
        print(line.strip("\n"), "NA")
    