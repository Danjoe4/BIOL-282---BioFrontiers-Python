# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:08:03 2021

@author: Daniel Broderick
"""
import os
from Bio import SeqIO 
import matplotlib.pyplot as plt


def main(proteome, file):
    # collect user input if necessary
    if proteome == None:
        proteome = input("Please provide the name of a \
                  Uniprot fasta file as input (A)")
    # doesn't matter if you include the file type 
    if proteome[-6:] == ".fasta":
        proteome = proteome[:-6]
    my_fasta = proteome + ".fasta" 
    # check that the file exists
    if not os.path.isfile(my_fasta):
        print("File not found")
        return
    
    if file == None:
        file = input("Please provide the name of a \
                  text file as input")
    # doesn't matter if you include the file type 
    if file[-4:] == ".txt":
        file = file[:-4]
    file = file + ".txt" 
    # check that the file exists
    if not os.path.isfile(file):
        print("File not found")
        return
    
    # gather the subset as a list
    with open(file, mode = 'r') as f:  
        subset = f.read().splitlines() 
        
    
    
    protdata = []
    # double list of the following format:
    # [[ID, protein sequence length, cysteine count, acidic AA count, 
    # basic AA count, hydrophobic AA count], .....]
    
    ##### parse ######
    fasta_file = SeqIO.parse(open(my_fasta),'fasta')
    with open(my_fasta, mode= 'r'):
        for fasta in fasta_file:
            length = len(fasta.seq)
            seq = fasta.seq
            protdata.append([fasta.id, length, seq.count('C'),
                             acidic(seq), basic(seq), hydrophobic(seq)])
         
    # extract the info for the subset IDs
    subdata = [x for x in protdata if x[0] in subset]
    
    
    ##### plot ############
    # create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2) 
    labels = 'Cysteine', 'Acidic', 'Basic', 'Hydrophobic', 'Other'
    
    # plot each pie chart in a separate subplot
    ax1.pie(proportion(protdata), labels = labels, autopct = '%.2f')
    ax2.pie(proportion(subdata), labels = labels, autopct = '%.2f')
    
    # add titles 
    fig.suptitle("Amino Acid Composition")
    ax1.set_title("Proteome")  
    ax2.set_title("Subset")
    
    plt.show() # show both piecharts
    
    

def proportion(data):
    """ calculate the percentage that the AAs make up and returns a list
    """
    length_sum = 0
    Cysteine_sum = 0
    Acidic_sum = 0
    Basic_sum = 0
    Hydrophobic_sum = 0
    
    for x in data:
        length_sum += x[1]
        Cysteine_sum += x[2]
        Acidic_sum += x[3] 
        Basic_sum += x[4]
        Hydrophobic_sum += x[5]
    
    Cysteine = Cysteine_sum/length_sum *100
    Acidic =  Acidic_sum/length_sum *100
    Basic = Basic_sum/length_sum *100
    Hydrophobic = Hydrophobic_sum/length_sum *100
    # so we get a nice even 100%
    Other = 100 - (Cysteine + Acidic + Basic + Hydrophobic)
    print()
    return [Cysteine, Acidic, Basic, Hydrophobic, Other]
    

def acidic(seq):
    """returns the count of aspartate (D) and Glutamic acid (E)
    """
    return seq.count('D') + seq.count('E')
        


def basic(seq):
    """combined count of Arginine (R), Histidine (H), and Lysine (K)
    """ 
    return seq.count('R') + seq.count('H') + seq.count('K')



def hydrophobic(seq):
    """What is considered hydrophobic seems not to be clear cut, I use this
    source: http://www.russelllab.org/aas/hydrophobic.html and only consider
    the very hydrophobic AAs, which are  Valine (V), Isoleucine (I), Leucine (L),
    Methionine (M), Phenylalanine (F), Tryptophan (W) and Cysteine (C)
    """ 
    return seq.count('V') + seq.count('I') + seq.count('L') + \
            seq.count('M') + seq.count('F') + seq.count('W') + seq.count('C')



if __name__ == "__main__":
    main("uniprot-proteome_UP000000625", 'subset.txt')