#!/usr/bin/env python3

import sys
series = open(sys.argv[1])


perfect_alignment = 0
for alignment in series:
    fields = alignment.split("\t")
    opt_cols = fields[11:]
    for col in opt_cols:
        if "NM:i:0" in col:
            perfect_alignment += 1
print(perfect_alignment)
