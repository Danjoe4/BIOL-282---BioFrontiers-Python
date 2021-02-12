# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:53:12 2021

@author: Daniel Broderick
"""

import Bio
# sudo pip3 install RamachanDraw
import RamachanDraw as RD

def main(PDB_id):
    path = RD.fetch(PDB_id) # searches and stores the PDB file
    RD.plot(path, 'prism') 
    # I like this color scheme the best, very pretty
     
    

    


if __name__ == "__main__":
    main("4YB9")