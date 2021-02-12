# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:55:17 2021

See my comments, this script may require you to download a local NCBI database,
it takes a couple minutes. 

I used ete3 because it had better documentation and a get_lineage function. 
Entrez was more confusing because it required me to use their custom classes.
ete3 lets me provide the ID and get a simple list of ancestor IDs

Also note that I did all the optional stuff for this exercise

@author: Daniel Broderick
"""
# install with::         pip install --upgrade ete3
from ete3 import NCBITaxa 
# or for conda do::      conda install -c etetoolkit ete3 ete_toolchain        

ncbi = NCBITaxa() # initialize

# uncomment the line below and run if you have issues, although you'll 
# probably already have the full database from some other student's code
# ncbi.update_taxonomy_database() 


def main(tax1, tax2):
    # create lineages
    lin1 = ncbi.get_lineage(tax1)
    lin2 = ncbi.get_lineage(tax2) 
        
    # find a recent common ancestor
    tmp1_ancest = find_RCA(lin1, lin2)
    # try it the other way
    tmp2_ancest = find_RCA(lin2, lin1)
    
    if tmp1_ancest is None:
        MRCA = tmp2_ancest
    elif tmp2_ancest is None:
        MRCA = tmp1_ancest
    else:
        # take the more recent ancestor
        MRCA = tmp1_ancest if (lin2.index(tmp1_ancest) > \
                           lin1.index(tmp2_ancest)) else tmp2_ancest
    
    
    # all the "if possible" exercise stuff 
    print(Extras(tax1))
    print(Extras(tax2))
    
    # I only return the id number, the rest is printed
    print("Their most recent common taxon is: " +      
            str(ncbi.get_taxid_translator([MRCA])[MRCA]) )
    return MRCA


def find_RCA(x, y):
    """ looks through all of lineage 2 for a possible match from lineage 1,
     then move up lineage 1"""
     
    for i in reversed(x):
        for j in reversed(y):
            if i == j:
                return i 


def Extras(taxa):
    """ returns a string of the Genus, Family and Order a taxa belongs to 
    """
    # taxa name
    specname = ncbi.get_taxid_translator([taxa])[taxa]
    
    
    # create lineage and dict of ranks
    lineage = ncbi.get_lineage(taxa) 
    ranks = ncbi.get_rank(lineage)
    # unfortunately the ranks are the values of the dict, so we do weird stuff
    # to get the taxaIDs from the dict 
    genus = list(ranks.keys())[list(ranks.values()).index('genus')]
    family = list(ranks.keys())[list(ranks.values()).index('family')]
    order = list(ranks.keys())[list(ranks.values()).index('order')]
    
    # convert taxa ID to a name 
    gname = ncbi.get_taxid_translator([genus])[genus]
    fname = ncbi.get_taxid_translator([family])[family]
    oname = ncbi.get_taxid_translator([order])[order]
      
    # return a big string
    return f"For {specname}, the genus is {gname}, the family is {fname} \
and the order is {oname} \n"
    
    
    


if __name__ == "__main__":
    # pass the taxa IDs to main
    main(3702, 3712)
