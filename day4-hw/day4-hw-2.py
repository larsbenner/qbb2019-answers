#!/usr/bin/env python3


"""usage: ./0 metadata.p <metadat.csv> <ctab> <ctabdir> ...
create all.csv with FPKMS
t_name, gene_name, sampel1,..,sample2"""

"""box plot all transcripts for a given gene"""

import sys
#create file paths correctly
import os
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")

goi = df.loc[:,"gene_name"] ==gene_name #get25 trues

fpkms=df.drop(columns="gene_name") #drops 2nd column so just have id and fpkms

col_names = fpkms.columns#makes variable columns
#
female_names=[]
for i in col_names:
  if "female" in i:
      female_names.append(True)
  else:
      female_names.append(False)
print(female_names)
#apends true and false to list depending on location
male_names=[]
for i in col_names:
  if "female" not in i:
      male_names.append(True)
  else:
      male_names.append(False)

#print(female_names)
#print(male_names)
#define ax1 and ax2 so on onew plot
fig, (ax1, ax2) =plt.subplots(nrows=2)
ax1.boxplot(fpkms.loc[goi, female_names].T)
ax2.boxplot(fpkms.loc[goi, male_names].T)
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xlabel("Stages of Development")
ax1.set_ylabel("FPKMs")
ax2.set_ylabel("FPKMs")
ax1.set_title("females")
ax2.set_title("males")
fig.suptitle("FPKMs by sex during development")
plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.savefig("boxplothw2.png")
plt.close(fig)

#earlier rough dragt of list method that doesnt work
# female_data_1 = samples.loc[:,"sex"] == "female"
# female_data_2 = samples.loc[:,"gene_name"] == "gene_name"
# #print(samples.loc[female_data_1 & female_data_2, :])
# female_data_list = list(samples.loc[female_data_1 & female_data_2, :])
#
#
#
# male_data_1 = samples.loc[:,"sex"] == "male"
# male_data_2 = samples.loc[:,"gene_name"] == "gene_name"
# #print(samples.loc[male_data_1 & male_data_2, :])
# male_data_list = list(samples.loc[male_data_1 & male_data_2,:])



