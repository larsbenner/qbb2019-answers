#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


t_name = sys.argv[1]
#/qUsers/cmdb/qbb2019/data/samples.csv
#data.samples csv
samples = pd.read_csv(sys.argv[2])


def sex_sorter(sex):
   soi = samples.loc[:,"sex"] == sex
   stages = samples.loc[soi,"stage"]
   # print(srr_ids)
   #load combined fpkms into data file
   fpkms = pd.read_csv(sys.argv[3],index_col="t_name")
   #extract data
   my_data =[]
   for stage in stages:
       # print(srr_id)
       my_data.append(fpkms.loc[t_name,sex+ '_' +stage])
   return my_data


male_data = sex_sorter("male")
female_data = sex_sorter("female")
# print(my_data)

# #code to plot additional replicates
# metadata = sys.argv[1]
# ctab_dir = sys.argv[2]
# #opening metadata and spliting it and in fields the sample and stage and sex
# #dictionary storing fpkms

# #reads in replicates.csv
# replicate_metadata = pd.read_csv(sys.argv[4])
# fpkms = {}
# for i, line in enumerate( open(replicate_metadata)):
#     if i == 0:
#         continue
#     fields = line.rstrip("\n").split(",")
#     srr_rep_id = fields[0]
#     descriptive_col = fields[1]+ "_" + fields[2]
#     ctab_path = os.path.join(ctab_dir, srr_id,
#                                    "t_data.ctab")

labels = ["Male","Female"]
labels2 = ["10","11","12","13","14A","14B","14C","14D"]
fig,ax = plt.subplots()
ax.plot(male_data, color = "blue")
ax.plot(female_data, color = "red")
ax.set_title("Male and Female mRNA abundance for Sxl Transcripts")
ax.set_xticklabels(labels2, rotation='vertical')
ax.set_xticks(np.arange(len(labels2)))
ax.set_ylabel("mRNA abundance")
plt.legend(labels=labels, loc="center left", bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)