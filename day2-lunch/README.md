

head -n 40000 /Users/cmdb/data/rawdata/SRR072893.fastq > SRR072893.10k.fastq
#first 10000 reads to a new file
fastqc SRR072893.10k.fastq
#generates QC reports
#map to ref genome, converts to sam
hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam 

samtools sort -O bam SRR072893.10k.sam > SRR072893.10k.bam 
samtools index SRR072893.10k.bam 