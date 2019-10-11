#!/usr/bin/env python3
#puts in mismatched gaps back in nucleotide files
import sys
from fasta import FASTAReader
reader = FASTAReader(open(sys.argv[1]))
reader2=FASTAReader(open(sys.argv[2]))
my_prot_sequence = [] #protein
for ident, sequence in reader:
  my_prot_sequence.append(sequence)
#print(my_sequence)
#quit()
my_sequence_nt=[] #nucleotide
for ident2,sequence2 in reader2:
   my_sequence_nt.append(sequence2)
#print(my_sequence_nt)
newlist=[]
for m in my_sequence_nt:
   #dna = my_sequence_nt[m]#you only need to do it in the query sequence
#store by sequence identity in dictionary
# for i in range(len(my_prot_sequence)):
   #dna= str(dna)
   for i in range(len(my_prot_sequence)):
     gap_dna = ""
     nucl_pos=0
     for num, a in enumerate(my_prot_sequence[i]):
         # print(a)
         if a == "-":
             gap_dna = gap_dna + "---"
         else:
             gap_dna = gap_dna + m[nucl_pos:nucl_pos+3]
             nucl_pos+=3
     newlist.append(gap_dna)
print(newlist)
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
