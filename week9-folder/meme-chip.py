#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np
sequence=open(sys.argv[2])
peaks=open(sys.argv[1])
output_file=open(sys.argv[3], 'w')
sequencetotal=""
position={}
for i,line in enumerate(peaks):
   fields=line.rstrip("\n").split()
   position[fields[3]]=[fields[1],fields[2]]
#print(position)
#    position[]
#quit()
for i in sequence:
   if i.startswith(">"):
       continue
   fields2=i.rstrip("\n")
   sequencetotal+=str(fields2)
#print(sequencetotal)
#quit()
sequencesident=[]
count=0
for key,value in position.items():
   #print(key)
   count+=1
   output_file.write('>{}\n{}\n'.format(count,(sequencetotal[int(value[0]):int(value[1])])))
output_file.close()

