#!/usr/bin/env python3
import sys
import numpy as np
# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
#              A     C     G     T
sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]
index = {'A':0,'C':1,'G': 2,'T':3}
gap = 300
s1 = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
s2 = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"
n=len(s1)
m=len(s2)
#print(n,m)
score_matrix= np.zeros((n+1,m+1))
traceback_matrix =np.zeros((n+1,m+1))
for i in range(n+1):
    score_matrix[i][0] = -gap * i
for j in range(m+1):
    score_matrix[0][j] = -gap * j
#print(j)
#print(traceback_matrix)
for i in range(1,n+1):
    for j in range(1,m+1):
        all_list = []
        h = score_matrix[i][j-1] - gap
        v = score_matrix[i-1][j] - gap
        d = score_matrix[i-1][j-1] + sigma[index[s1[i-1]]][index[s2[j-1]]]
        all_list.append(h)
        all_list.append(v)
        all_list.append(d)
#print(h, v, d)
#print(all_list)
        score_matrix[i,j]= max(all_list)
        #print(all_list)
        traceback_matrix[i,j]=all_list.index(max(all_list))
#print(traceback_matrix)
#print(score_matrix)
i=len(s1)
j=len(s2)
seq1_align=""
seq2_align=""
while j != 0 and i != 0:
    t = traceback_matrix[i,j]
    if t == 0: 
         seq1_align+="-"
         seq2_align+=str(s1[i-1])
         j = j - 1
    elif t==1:
        seq1_align+=str(s2[j-1])
        seq2_align+="-"
        i = i - 1
    else:
        seq1_align+=str(s1[i-1])
        seq2_align+=str(s2[j-1])
        i = i - 1
        j = j - 1
print(seq1_align[::-1])
print(seq2_align[::-1])
print(score_matrix[len(s1),len(s2)])