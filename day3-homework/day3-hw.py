#!/usr/bin/env python3


"""count all kmers in fasta file"""

from fasta import FASTAReader
import sys
#!/usr/bin/env python3

#this is a class?
target_reader = FASTAReader(open(sys.argv[1]))
query_reader = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

target_dict = {}
for ident, sequence in target_reader:
    sequence = sequence.upper()
    for i in range (0, len(sequence) -k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else:
            target_dict[kmer] = [(ident, i)]
            
#print(target_dict)

#query_dict = {}
for ident, sequence in query_reader:
    sequence = sequence.upper()
    for i in range (0, len(sequence) -k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            for ident, j in target_dict[kmer]:
                print(ident, j, i, kmer)
            
#print(query_dict)

#match = set(target_dict.keys()).intersection(set(query_dict.keys()))

#print(match)

#for t in match:
    #print (target_dict[t], query_dict[t], i)
    
    
          
        


    







#this is a class?
#reader = FASTAReader (sys.stdin)
#k = int(sys.argv[1])

#want kmer and corresponding count

#kmers = {}
#for ident, sequence in reader:
    #sequence = sequence.upper()
    #for i in range (0, len(sequence) -k + 1):
        #kmer = sequence[i:i+k]
        #if kmer in kmers:
            #kmers[kmer] += 1
        #else:
            #kmers[kmer] = 1
#gets you tuple           

#def get_count(t):
    #return[1]

#for kmer, count in sorted(kmers.items(),
                          #key=lambda t: t[1]):
    #print(kmer, count, sep="\t")