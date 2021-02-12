# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:20:33 2021

Exercise 4

Please place the Uniprot fasta file in the same folder as the script. You 
might get errors simply piping the fasta to the script via terminal and I don't
know what your PATH looks like so this should be most convenient. Also, DELETE
OUTPUT FOLDERS AFTER EACH TEST otherwise you will get a FileExistsError.

Yes I didn't compartmentalize code into functions because I didn't want to 
deal with passing sequence objects. 

@author: Daniel Broderick
"""
from Bio import SeqIO
from Bio import Blast
import os
import sys

def main(my_fasta, datafiles = None):
    """"Please provide the name of a  
    Uniprot fasta file as input (A) and any number of Uniprot
    fasta files (B) as a list. This script doesn't check file format so make
    sure to include .fasta in the my_fasta file string, and no extension for
    the data files list (also, those datafiles should have already have their 
    databases created, which should be in the base directory).

    """
    basedir = os.getcwd() # useful for later
    
    
    # check that the file exists
    if not os.path.isfile(my_fasta):
        print("File not found")
        sys.exit()
        
    ############ PART C: output folders #########
    folderslist = []
    
    count = 0
    fasta_file = SeqIO.parse(open(my_fasta),'fasta')
    with open(my_fasta, mode= 'r'):
        for fasta in fasta_file:
            count +=1
    
    fullfolders = count //1000 
    for i in range(fullfolders):
        # yes this gives you leading zeros but its comphrehensible
        os.mkdir(f"{i}001 - {i+1}000")
        folderslist.append(f"{i}001 - {i+1}000")
    #last folder
    if count%1000 != 0:
        zerocount = str(0) * (3- len(str(2777%1000)))
        os.mkdir(f"{fullfolders}001 - {fullfolders}{zerocount}{count%1000}")
        folderslist.append(f"{fullfolders}001 - {fullfolders}{zerocount}{count%1000}")
    
    
    if not os.path.exists(folderslist[0]):
        os.mkdir(folderslist[0])
        
    indxct = 0
    foldindx = 0
    # open and stream the file
    fasta_file = SeqIO.parse(open(my_fasta),'fasta')
    with open(my_fasta, mode= 'r'):
        for fasta in fasta_file:
            # change folders every thousand fastas
            indxct += 1
            if indxct > 1000*foldindx +1000:
                foldindx +=1 
                
            ID = fasta.id.replace('|', '-') #use a valid symbol
             
            os.chdir(folderslist[foldindx]) # where our output goes
            ##### partA #####  Write a fasta file called ID + “.fasta” 
            # within a directory called ID. 
            # make the directory
            if not os.path.exists(ID):
                os.mkdir(ID)
                print("Directory " , ID ,  " Created ")
            else:    
                print("Directory " , ID ,  "already exists")
                
            # go inside the directory
            try:
                os.chdir(ID)
            except OSError:
                print("cant change directory")
            
            # write the fasta 
            SeqIO.write(fasta, ID + ".fasta", "fasta")
            
            ############ part B: write the job/blast file  #############
            # create the blast command 
            blast = ""
            for x in datafiles:
                blast += f"blastp -db {x} -query {my_fasta} -out {x}comparison.out \n"
            print(blast)
            # write to a job file, will overwrite existing files
            jf = open(ID + ".job", "w") 
            jf.write(blast)
            jf.close()
            
            #reset to base directory
            os.chdir(basedir)



    






if __name__ == "__main__":
    main("uniprot-big-proteome_UP000000625.fasta", ["uniprot-proteome_UP000464024",
                                                    "threeseqtest.fasta"])