#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:15:25 2023
searching entries in GENBANK db 
@author: nikos
"""

from Bio import Entrez
query=input()
start=input()
end=input()
Entrez.email = "nikoverg@biol.uoa.com"
handle = Entrez.esearch("nucleotide", "{}[Organism]".format(query), datetype="pdat", mindate=start, maxdate=end)
record = Entrez.read(handle)
record["Count"]
