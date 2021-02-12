# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:04:16 2021

@author: Daniel Broderick
""" 
from Bio import SeqIO 
import os
# import sys
# import numpy as np

def main(proteome, acid):
     
    # collect user input if necessary
    if proteome == None:
        proteome = input("Please provide the name of a \
                   fasta file as input")
    # doesn't matter if you include the file type 
    if proteome[-6:] == ".fasta":
        proteome = proteome[:-6]
    my_fasta = proteome + ".fasta" 
    # check that the file exists
    if not os.path.isfile(my_fasta):
        print("File not found")
        return
    
    data = []
    # a double list of the following format:
    # [[ID, protein length, aminoacid count, amindoacid %], .....]
    
    ##### parse ######
    fasta_file = SeqIO.parse(open(my_fasta),'fasta')
    with open(my_fasta, mode= 'r'):
        for fasta in fasta_file:
            length = len(fasta.seq)
            pc = fasta.seq.count(acid)
            data.append([fasta.id, length, pc, pc/length])
            
    # sort by the protein length
    data.sort(key = lambda a: a[1])
    
    ###### list of IDs and total amino acid count of the 80th percentile ####
    ID80 = []
    acid80 = 0 
    for i in range(round(.8 * len(data))):
        ID80.append(data[i][0])
        acid80 += data[i][2]
    
    # 20th percentile
    ID20 = []
    acid20 = 0 
    for i in range(round(.8 * len(data)), len(data)):
        ID20.append(data[i][0])
        acid20 += data[i][2] 
    
    
    #more or less of the acid
    more_less = 'more' if acid20>acid80 else 'less'
    
    out = f"The top 20% longest proteins have {acid20} {acid}'s, which is \
{more_less} than the {acid80} {acid}'s in the remaining 80% of proteins" 
    print(out) 
    return ID80, ID20
    
    



if __name__ == "__main__":
    main("uniprot-proteome_UP000000625", 'A')