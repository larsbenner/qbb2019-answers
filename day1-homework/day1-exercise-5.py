#!/usr/bin/env python3

import sys
series = open(sys.argv[1])


total = 0
count = 0
for alignment in series:
    fields = alignment.split("\t")
    if fields[2] == "*":
         continue
    else:
        total = total + int(fields[4])
        count += 1
avg_map_q_score = total / int(count)

print(avg_map_q_score)

#removing reads that didn't map