#!/usr/bin/env python3
import sys
#use CpG_context_SRR files
fileS52=open(sys.argv[1])
fileS54=open(sys.argv[2])
list1=[]
counter=0
counter2=0
list2=[]
unique=[]
list11=[]
list22=[]
for i,line in enumerate(fileS52):
    if line.startswith("track"):
        continue
    fields1=line.rstrip("\n").split()
    if float(fields1[3])>=50:
        list1.append(fields1[1])
    if float(fields1[3])<50:
        list11.append(fields[1])
#print(list1)
for j,lines in enumerate(fileS54):
    if lines.startswith("track"):
        continue
    fields2=lines.rstrip("\n").split()
    if float(fields1[3])>=50:
        list2.append(fields2[1])
    if float(fields1[3])<50:
        list22.append(fields2[1])
for a in list2:
    if a not in list1:
        unique.append(a)
        counter+=1
#print(list2)
print(counter)
#print(fields1)
