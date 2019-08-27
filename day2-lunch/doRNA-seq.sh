#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -O bam $SAMPLE.sam > $SAMPLE.bam
  samtools index -b $SAMPLE.bam
  stringtie $SAMPLE.bam -e -B -p $THREADS -G $ANNOTATION -o $SAMPLE.gtf
done
