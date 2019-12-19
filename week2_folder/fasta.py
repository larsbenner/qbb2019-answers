#!/usr/bin/env python3
# from Fasta import FASTAReader

"""
Parse and print all records from a FASTA file
"""

import sys

class FASTAReader( object ):
    
    def __init__( self, fh ):
        self.fh = fh
        self.last_ident = None
        self.eof = False

    def __iter__( self ):
        return self

    def __next__( self ):
        
        if self.eof:
            #return None, None
            raise StopIteration
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
        # If we reach here, ident is set correctly
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append( line.strip() )
                
        sequence = "".join( sequences )
        return ident, sequence


reader = FASTAReader(open(sys.argv[1]))

print (reader)

list_seq=[]
    
for ident, sequence in reader:
    list_seq.append(sequence)
    list_seq.sort(key=len, reverse=True)
    
#print(list_seq)

#average of contigs
sum = 0
count = 0


longest = len(list_seq[0])
shortest = len(list_seq[-1])

for seq in list_seq:
    sum += len(seq)
    count +=1
    
average = sum/count
#print(average)    

total_length = 0
#gets n50 value
for i, item in enumerate(list_seq):
    total_length += len(item)
    if total_length >= sum/2:
        break
n50_value = len(list_seq[i])
#prints all the 4 values
print ("the longest contig is " + str(longest))
print("the shortest contig is " + str(shortest))
print("the average contig length is " + str(average))
print ("the n50 value is " + str(n50_value))
print ("number of contigs is " + str(count))
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    