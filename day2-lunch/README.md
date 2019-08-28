

head -n 40000 /Users/cmdb/data/rawdata/SRR072893.fastq > SRR072893.10k.fastq
#first 10000 reads to a new file
fastqc SRR072893.10k.fastq
#generates QC reports
#map to ref genome, converts to sam
hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam 
#converts sam to bam and indexes
samtools sort -O bam SRR072893.10k.sam > SRR072893.10k.bam 
#indexes bam file
samtools index -b SRR072893.10k.bam 
#-o allows to creats subdirectory
stringtie SRR072893.10k.bam  -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o SRR072893.10k.sorted.gtf


#!/bin/bash


#prints 3rd column#
#!/bin/bash
rm temp.sam
grep "^SRR072893" SRR072893.10k.sam > temp.sam
rm chromo.txt
awk '{print $3}' temp.sam | sort | uniq -c > chromo.txt


#searches for lines that start with SRR... and outputs that 
#to a file called temp.sam amd prints 3rd column
#and sorts and counts unique chromosomes which is in column 3
#and puts to a chrom.txt file

awk '{print NF}' temp.sam | sort | uniq -c > unique_cols.txt


# prints number of fields
#and sorts and counts unique field size 
#and puts to a chrom.txt file