#!/usr/bin/env python3


"""count all kmers in fasta file"""

from fasta import FASTAReader
import sys
#!/usr/bin/env python3

#this is a class?
target_reader = FASTAReader(open(sys.argv[1]))
query_reader = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

chrom_dict = {}
target_kmer_dict = {}
for ident, target_seq in target_reader:
    target_seq = target_seq.upper()
    len_target_seq = len(target_seq)
    chrom_dict[ident] = target_seq
    j = 0
    for i in range(0, len(target_seq) -k + 1):
        kmer = target_seq[j : (j+k)]
        #print(ident, kmer)
        j = j + 1
        if kmer not in target_kmer_dict:
            target_kmer_dict[kmer] = [[ident, j - 1 ]]
        else:
            target_kmer_dict[kmer].append([ident, j - 1])
#print (chrom_dict)

# for key in target_kmer_dict:
#     print(key, target_kmer_dict[key])
# for key in chrom_dict:
#     print(key, chrom_dict[key])




#j is target start i is query start
# target_sequen = {}
#
# final_dict = {}
# #will be kmer dictionary
# kmer_dict = {}
#
#
#
#     print(ident)
#     target_sequence = target_sequence.upper()
#     #adding suquence to a new dictionary called target_sequen and uses ident
#     target_sequen[ident] = target_sequence
#     for j in range (0, len(target_sequence) -k + 1):
#         #makes kmer
#         kmer = target_sequence[j:j+k]
#         print(kmer)
#         #appends
#         if kmer in target_dict:
#             kmer_dict[kmer].append((ident, j))
#         else:
#             kmer_dict[kmer] = [(ident, j)]
#
#print(target_dict)
#print(target_kmer_dict)
query_dict = {}
#searches for kmers and extends if match
final_dict = {}
for ident, query_seq in query_reader:
    query_seq = query_seq.upper()
    for i in range (0, len(query_seq) -k + 1):
        kmer = query_seq[i : i+k]
        if kmer in target_kmer_dict:
            for position in target_kmer_dict[kmer]:
                length = 12
                extend_right = True
                while extend_right == True:
                    temp_kmer = query_seq[i : i + length]
                    query_kmer = chrom_dict[position[0]][position[1] : position[1]+length]
                    if position[1]+length == len(chrom_dict[position[0]]) or query_seq[i : i + length] == len(query_seq):
                        extend_right = False
                        final_dict[temp_kmer] = [position[0], position[1]]
                    elif query_kmer == temp_kmer:
                        length +=1
                        temp_kmer = query_seq[i : i + length]
                        query_kmer = chrom_dict[position[0]][position[1] : position[1]+length]
                    else:
                        extend_right = False
                        final_dict[temp_kmer] = [position[0], position[1]]
for key in final_dict:
    print(len(key), key, final_dict[key][0])                        
                        
                        
                        
              
#













