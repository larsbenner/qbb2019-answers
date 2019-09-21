#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
af = []
dp = []
qual_list = []
qual_list = []
count = 0
count_new = 0
count_2 = 0
ann_score = []
ann_dict = {}
for line in open(sys.argv[1]): #snpeff
   if line.startswith("#"):
       continue
   fields = line.rstrip("\t").split()
   chrom = fields[0]
   pos = fields[1]
   ref_base = fields[3]
   alt_base = fields[4]
   qual_score = fields[5]
   qual_list.append(int(float(fields[5])))
   #new_qual_list = [round(x) for x in qual_list]
   info = fields[7]
   
   dp_split=info.split(";")[7]
   dp1 = dp_split.split("=")[1]
   dp.append(dp1)
   
   af_split = info.split(";")[3]
   af.append(af_split.split("=")[1])
   
   # ann_split =  info.split(";")[41]
   # ann_value = ann_split.split("=")[1]
   # ann_score.append(ann_value.split("|")[1])
   ann_split =  info.split(";")[41]
   ann_value = ann_split.split("=")[1]
   ann_score = ann_value.split("|")[1]
   if ann_score in ann_dict:
       ann_dict[ann_score] += 1
   else:
       ann_dict[ann_score] = 1
       
#print(ann_dict)


#print(type(ann_score))
#    if "upstream_gene_variant" in ann_score:
#        count +=1
# print(count)

#    if "synonymous_variant'" in ann_score:
#        count_new +=1
# print(count_new)
#
   
# fig, ax0 = plt.subplots()
# ax0.hist(dp, bins=100)
# fig.savefig( "dp" )
# plt.close(fig)
#
# fig, ax1 = plt.subplots()
# ax1.hist(qual_list, bins=100, range=[0, 2000])
# fig.savefig( "qual.png" )
# plt.close(fig)
#
# fig, ax = plt.subplots(4)
# ax2.hist(af, bins=100, range=[0, 50])
# fig.savefig( "af.png" )
# plt.close(fig)
#
# #Summary of Predicted Effects
# plt.bar(range(len(ann_dict)), list(ann_dict.values()), align = 'center')
# plt.xticks(range(len(ann_dict)), list(ann_dict.keys()))
# plt.xticks(range(len(ann_dict)), list(ann_dict.keys()), rotation = 'vertical', size = 5)
# plt.show()


fig, ax = plt.subplots(4)
ax[0].hist( dp, bins=100)
ax[1].hist( qual_list, bins=1000, range=[0,5000])
ax[2].hist( af, bins=100 )
plt.bar(range(len(ann_dict)), list(ann_dict.values()), align = 'center')
plt.xticks(range(len(ann_dict)), list(ann_dict.keys()), rotation = 'vertical', size = 5)
ax[0].set_xlabel("Variants")
ax[0].set_ylabel("Read Depth")
ax[1].set_xlabel("Variants")
ax[1].set_ylabel("Quality")
ax[2].set_xlabel("Variants")
ax[2].set_ylabel("Frequency")
ax[3].set_xlabel("Impact")
ax[3].set_ylabel("Frequency")
ax[0].set_title("Graph1-Read Depth")
ax[1].set_title("Graph2-Quality")
ax[2].set_title("Graph3-Allele Frequency")
ax[3].set_title("Graph4-Impact")
fig.savefig( "results.png" )
plt.close(fig)

   
   
   
       
       
