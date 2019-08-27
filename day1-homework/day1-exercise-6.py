#!/usr/bin/env python3

import sys
series = open(sys.argv[1])


total = 0
pos_range = list(range(10000, 20001))
for alignment in series:
    fields = alignment.split("\t")
    if fields[2] == "2L":
        if int(fields[3]) in pos_range:
            total += 1

print(total)
