#!/usr/bin/env python3

"""usage: <ctab1><ctab2> """

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
# #n freq >0
# count = 0
# fixed = FALSE
# #allele_freq = end_freq --> spit out # of gens from here
# while not fixed(start_freq =! 0 or 1), run this -> gen counter and fixed in while
# while inside function


# def fisher_model(start_freq, pop):
#     gen_count = 0
#     while True:
#         end_freq = np.random.binomial(2*pop, start_freq)/(2*pop)
#         gen_count += 1
#         if end_freq == 0 or end_freq == 1:
#             return gen_count
#         else:
#             start_freq = float(end_freq)
#
# fixation_times = []
# for i in range(1000):
#     fixation_times.append(fisher_model(.5, 100))

# fixation_times2 = {}
# means = []
# standard_dev = []
# pop_sizes = [100, 1000, 10000]
# for pop_size in pop_sizes:
#     fixation_times2[pop_size] = []
#     for i in range(1):
#         fixation_times2[pop_size].append(fisher_model(.5, pop_size))
# print (fixation_times2)

# for pop_size in pop_sizes:
#     means.append(np.mean(fixation_times2[pop_size]))
# for pop_size in pop_sizes:
#     standard_dev.append(np.std(fixation_times2[pop_size]))
    
    
# fig, ax = plt.subplots()
# ax.bar([x for x in range(1,len(pop_sizes)+ 1)], means, ecolor='black')
# ax.set_xticks(([x for x in range(1,len(pop_sizes)+ 1)]))
# ax.set_xticklabels(["100","1000","10000"])
# ax.set_xlabel("Population Size")
# ax.set_ylabel("Generation Time")
# ax.set_title("Generation Time as a function of Population Size")
# fig.savefig("bar.png")
# plt.close(fig)
# plt.show()

# fixation_times3 = {}
# means1 = []
# standard_dev1 = []
# afs = [.2, .4, .6, .8]
# for af in afs:
#     fixation_times3[af] = []
#     for i in range(100):
#         fixation_times3[af].append(fisher_model(af, 100))
# print (fixation_times3)
# #
# for af in afs:
#     means1.append(np.mean(fixation_times3[af]))
# for af in afs:
#     standard_dev1.append(np.std(fixation_times3[af]))
#
# fig, ax = plt.subplots()
# ax.bar([x for x in range(1,len(afs)+ 1)], means1, ecolor='black')
# ax.set_xticks(([x for x in range(1,len(means1)+ 1)]))
# ax.set_xticklabels([".2",".4",".6",".8"])
# ax.set_xlabel("Allele Frequency")
# ax.set_ylabel("Generation Time")
# ax.set_title("Generation Time as a function of Allele Frequency")
# fig.savefig("bar1.png")
# plt.close(fig)
# plt.show()


def fisher_model_selection(start_freq, pop, selection_coefficient):
    gen_count = 0
    while True:
        allele_count = start_freq * pop * 2
        prob = (allele_count * (1+selection_coefficient)) / ((2*pop) - (allele_count) + (allele_count*(1+selection_coefficient)))
        end_freq = np.random.binomial(2*pop, start_freq)/(2*pop)
        gen_count += 1
        if end_freq == 0 or end_freq == 1:
            return gen_count
        else:
            start_freq = float(end_freq)
            
fixation_times4 = {}
means2 = []
standard_dev2 = []
sel_list = [0,.2,.4,.6,.8,1]

for sel in sel_list:
    fixation_times4[sel] = []
    for i in range(100):
        fixation_times4[sel].append(fisher_model_selection(.5, 100, sel))
print (fixation_times4)
#
for sel in sel_list:
    means2.append(np.mean(fixation_times4[sel]))
for sel in sel_list:
    standard_dev2.append(np.std(fixation_times4[sel]))
    
fig, ax = plt.subplots()
ax.bar([x for x in range(1,len(sel_list)+ 1)], means2, ecolor='black')
ax.set_xticks(([x for x in range(1,len(means2)+ 1)]))
ax.set_xticklabels(["0",".2",".4",".6",".8","1"])
ax.set_xlabel("Selection Coefficient")
ax.set_ylabel("Generation")
ax.set_title("Generation Time as a function of Allele Frequency")
fig.savefig("bar2.png")
plt.close(fig)
plt.show()
    


# for i in range(100):
#     fixation_times4.append(fisher_model_selection(.5, 100, sel_list))
#
# print(fixation_times4)
#
# fixation_times4 = {}
# means2 = []
# standard_dev2 = []
# sel_list = [0,.2,.4,.6,.8,1]

#print (fixation_times)
#histogram fixation times 

# fig, ax = plt.subplots()
# ax.hist(fixation_times, bins=101, density = True)
# ax.set_xlabel("Number of Generations")
# ax.set_ylabel("Frequency")
# ax.set_title("Number of Generations to Fixation")
# fig.savefig("gen1.png")
# plt.close(fig)
    
    
    # for i in range(pop):
    #     while allele_freq =! 1
    #     end_freq = 2*pop
    #     count = 0
    #     fixed = FALSE
    #     r = random.random()
    #     if start_freq > r:
    #         end_freq += 1/pop
            
###fixed = FALSE
###if n_freq = 0 or 1: print count

    
    


