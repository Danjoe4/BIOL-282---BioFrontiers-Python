# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:18:36 2021

Sorry if the final output isn't the clearest, I couldn't figure out an easy
way to make the dots different colors

@author: Daniel Broderick
"""
from Bio import SeqIO
import os
import numpy

# plot
import matplotlib.pyplot as plot 
 
# needed for the calculations  
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def main(a = None):
    
    # collect user input if necessary
    if a == None:
        a = input("Please provide the name of a \
                  Uniprot fasta file as input (A)")
    # doesn't matter if you include the file type 
    if a[-6:] == ".fasta":
        a = a[:-6]
    my_fasta = a + ".fasta" 
    # check that the file exists
    if not os.path.isfile(my_fasta):
        print("File not found")
        return
        
    
    # we make a list of lists, with 4 values (1 bool and 3 floats) for each key
    # example [ ...
    # [hilight, weight, Isoelectric, Instability]
    # ....]
    
    ############## iterate #########################
    data = []
    fasta_file = SeqIO.parse(open(my_fasta),'fasta')
    with open(my_fasta, mode= 'r'):
        for fasta in fasta_file:     
            seq = str(fasta.seq).replace('X', 'N').replace('U','C')
            ProtData = ProteinAnalysis(seq)
                 
            # add the list entry 
            data.append([True if 'DNA' in fasta.description else False, 
                            ProtData.molecular_weight(),
                            ProtData.isoelectric_point(),
                            ProtData.instability_index()])
    
    ############### plot the data ########################
    plot.figure()
    ax = plot.axes(projection ="3d") 
    
    # use list comprehension to take appropriate elements
    # blue dots
    x1,y1,z1 = [x[1] for x in data if x[0] == False], \
    [y[2] for y in data if y[0] == False], [z[3] for z in data if z[0] == False]
    #red (highlighted) dots
    x2,y2,z2 = [x[1] for x in data if x[0] == True], \
    [y[2] for y in data if y[0] == True], [z[3] for z in data if z[0] == True]
    
    
    ax.scatter3D(x1, y1, z1, color = 'cyan', alpha = .1)
    ax.scatter3D(x2, y2, z2, color = 'red', alpha = 1)
    
    
    
    #labels
    plot.title("Molecular Weight vs Isoelectric Point vs Instability Index")
    ax.set_xlabel('Molecular Weight', fontweight ='bold')
    ax.set_ylabel('Isoelectric Point', fontweight ='bold')
    ax.set_zlabel('Instability Index', fontweight ='bold')
     
    
    plot.show()
    print(f"we have {len(data)} points, {len(x1)} of which are highlighted \
          (red), or {round(len(x1)/len(data) * 100, 2)}%")
   
        
            





if __name__ == "__main__":
    main("uniprot-proteome_UP000000625.fasta")