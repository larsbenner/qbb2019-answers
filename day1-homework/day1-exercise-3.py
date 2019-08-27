#!/usr/bin/env python3

import sys
series = open(sys.argv[1])


hits_with_one_location = 0
for alignment in series:
    fields = alignment.split("\t")
    opt_cols = fields[11:]
    for col in opt_cols:
        if "NH:i:1" in col:
            hits_with_one_location += 1
print(hits_with_one_location)