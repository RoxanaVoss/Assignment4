#!/usr/bin/env python3

#usage: 
#go in gitbash
#go in to right folder
#python as4_rv.py *.fasta

import glob
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import sys

#creating a sequence
#method to count kmers of size k
def count_kmers(seq):
    kmer_list=[]
    for i in range(len(seq)):
        if len(seq[i:i+k])==k:
            kmer=seq[i:i+k]
            kmer_list.append(kmer)
        else:
            pass
    return(kmer_list)
	
#producing a graph
def plot_kmer_freq(counter):	
	w = range(len(counter))
	values = counter.values()
	plt.figure(figsize = (10,4))
	plt.bar(w, values, trick_label = key);
	plt.savefig('kmer_freq.png')
	
counter={}
kmerdict=defaultdict(list)
#k specified as a argument
k=int(input("What size for kmer do you want to observe? "))
for filename in glob.glob('*fasta'):
    f=open(filename,'r')
    for row in f:
		#getting the species name
        if ">" in row:
            name=row.split(">")[1].split("\n")[0]
            continue
		#gettimg the sequence row
        if len(row)<=1:
            continue
        seq=row.rstrip("\n")
        kmer_list=count_kmers(seq)
        kmerdict[name].append(kmer_list)
#frame containing k and the associated number of observed and expected kmers 
print("{}\t{}\t{}\t{}\t{}".format("Species", "k", "Poss Kmers", "Obs Kmers", "Linguistic Complexity"))
for key, value in kmerdict.items():
	value=value[0]
	w=range(len(counter))
	pk=len(value)
	ok=len(set(value))
	#calculate Linguistic Complexity
	lc=ok/pk
	print("{}\t{}\t{}\t{}\t{}".format(key, k, ok, pk, lc))
	plot_kmer_freq(counter)