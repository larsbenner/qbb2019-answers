#!/usr/bin/env python3

import sys
series = open(sys.argv[1])


count = 0
for alignment in series:
    while count < 11:
        fields = alignment.split("\t")
        chromosome = fields[2]
        count += 1
        print(chromosome)