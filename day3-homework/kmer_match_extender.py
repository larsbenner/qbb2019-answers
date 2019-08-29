#!/usr/bin/env python3


"""count all kmers in fasta file"""

from fasta import FASTAReader
import sys
#!/usr/bin/env python3

#this is a class?
target_reader = FASTAReader(open(sys.argv[1]))
query_reader = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

#j is target start i is query start
target_sequen = {}

final_dict = {}
#will be kmer dictionary
kmer_dict = {}
for ident, target_sequence in target_reader:
    target_sequence = target_sequence.upper()
    sequence = target_sequen[ident]
    for j in range (0, len(target_sequence) -k + 1):
        #makes kmer
        kmer = target_sequence[j:j+k]
        if kmer in target_dict:
            kmer_dict[kmer].append((ident, j))
        else:
            kmer_dict[kmer] = [(ident, j)]
            
#print(target_dict)

#query_dict = {}
for ident, query_sequence in query_reader:
    query_sequence = query_sequence.upper()
    for i in range (0, len(query_sequence) -k + 1):
        kmer = query_sequence[i:i+k]
        if kmer in target_dict:
            for ident, j in target_dict[kmer]:
                target_seq = target_sequence[ident]
                len_target_seq = len(target_seq)
                query_target_seq = len(query_sequence)
                extend_right = True
                extended_kmer = kmer
                while True:
                    if extend_right:
                        #verify these are right
                        if query_sequence[i+k+1] == target_seq[j+k+1]:
                            i += 1
                            j += 1
                            extended_kmer += query_sequence[i+k+1]
                        else:
                            extend_right = False
                    else:
                        #this is where I add to my dictionary the extension
                        final_dict[extended_kmer].append(ident, i)]
                        break
                    if (j+k == len_target_seq) or (i+k == query_target_sequence):
                        extend_right = False
                    
                    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                            
               
                                                                                                                                                                                                           
            