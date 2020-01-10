#!/usr/bin/env python3

import sys
from fasta import FASTAReader
import math
import matplotlib.pyplot as plt
import statistics as stats

reader = FASTAReader(open(sys.argv[1])) #translated.out

protein_seq = []
for ident, sequence1 in reader:
   protein_seq.append(sequence1)

#print (protein_seq)  
reader2 = FASTAReader(open(sys.argv[2])) #3_new_blast_output

nt_seq = []
for ident, sequence2 in reader2:
   nt_seq.append(sequence2)

#print (nt_seq)

list1 =[]
for sequence, protein in zip(nt_seq, protein_seq):
     dna1 = ""
     nt_pos=0
     for num, j in enumerate(protein):
         # print(a)
         if j == "-":
             dna1= dna1 +"---"
         else:
             dna1 = dna1 + sequence[nt_pos:nt_pos+3]
             nt_pos+=3
     list1.append(dna1)
# print(list1)

codons = {
     "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
     "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
     "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
     "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
     "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
     "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
     "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
     "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
     "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
     "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
     "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
     "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
     "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
     "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
     "TAC":"Y", "TAT":"Y", "TAA":"", "TAG":"",
     "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W"}

query = list1[0]
rest_of_dna = list1[1:]

#print(query)
#print (rest_of_dna)

dSyn_list=[]
dNon_list=[]

for i in range(0, (len(query)), 3):
    dSyn = 0
    dNon = 0
    #print(query[i:i+3])
    if query[i:i+3] == '---':
        continue
    for sequence in rest_of_dna:
        if sequence[i:i+3] == '---':
            continue
        if sequence[i:i+3] not in codons:
            continue
        if query[i:i+3] != sequence[i:i+3] and codons[query[i:i+3]] == codons[sequence[i:i+3]]:
            dSyn += 1
        if query[i:i+3] != sequence[i:i+3] and codons[query[i:i+3]] != codons[sequence[i:i+3]]:
            dNon += 1
    dSyn_list.append(dSyn)
    dNon_list.append(dNon)
    
# print(dSyn_list)
#print(dNon_list)

ratioSN = []
for i in range(len(dSyn_list)):
    ratio = (dSyn_list[i] +1)/ (dNon_list[i]+1)
    log_ratio = math.log2(ratio)
    ratioSN.append(ratio)

#print (ratioSN)

diffSN = []
for i in range(len(dSyn_list)):
    differ = dSyn_list[i]-dNon_list[i]
    diffSN.append(differ)

#print(diffSN)
stdev_diff = stats.stdev(diffSN)
#print (stdev_diff)
z_score = []
for i in diffSN:
    zscore = i/stdev_diff
    z_score.append(zscore)
# print(z_score)

colors = ['red' if zscore > 1.645 or zscore<-1.645 else 'black'for zscore in z_score]
fig, ax = plt.subplots()
ax.scatter([x for x in range(len(z_score))], ratioSN, color=colors, s=2)
ax.set_xlabel('position')
ax.set_ylabel('log2(dN/dS)')

fig.savefig("final_plot.png")
plt.close(fig)
   #dna = my_sequence_nt[m]#you only need to do it in the query sequence
#store by sequence identity in dictionary
# for i in range(len(my_prot_sequence)):
   #dna= str(dna)
  
 #print(len(gap_dna))
 #print("~~~~~~~~~~")
 #print(len(my_prot_sequence[0]))
#print(s)
#print(my_sequence_nt)



#print(my_sequence_nt)

# nucl_pos = 0
# for seq_id in my_dict:
#     new_line = ''
#     prot_seq = my_dict[seq_id][0]
#     nucl_seq = " " [1]
#     for char in prot_seq:
#         if char == '-':
#             new_line += '---'
#
#         else:
#             new_line += nucl_seq[nucl_pos:nucl_pos + 3]
#             nucl_pos += 3
