#!/bin/bash
rm *sorted.*
for i in *bed
do
    bedtools sort -i $i > ${i%.bed}.sorted.bed
done

bedtools sort -i k4me3.bed > k4me3.sorted.bed
bedtools sort -i k27me3.bed > k27me3.sorted.bed
bedtools sort -i k9me3.bed > k9me3.sorted.bed


rm *jaccard.txt*
echo '*** k4me3 vs k9me3' >> jaccard.txt
bedtools jaccard -a k4me3.sorted.bed -b k9me3.sorted.bed >> jaccard.txt
echo '*** k27me3 vs k4me3' >> jaccard.txt
bedtools jaccard -a k27me3.sorted.bed -b k4me3.sorted.bed >> jaccard.txt
echo '*** k27me3 vs k9me3' >> jaccard.txt
bedtools jaccard -a k27me3.sorted.bed -b k9me3.sorted.bed >> jaccard.txt

rm *annot*
bedtools closest -d -t first -a k4me3.sorted.bed -b genes.bed > temp.bed
awk '{print $1"\t"$2"\t"$3"\t"$7"\t"$8}' temp.bed > k4me3.annot.bed
tail -10 k4me3.annot.bed > k4me3.annot.last.bed
rm temp.bed

rm *annot.most.bed
bedtools coverage -a k4me3.annot.bed -b /Users/cmdb/qbb2019-answers/results/SRR072893.bam | sort -k6 -n | tail -10 > k4me3.annot.most.bed
