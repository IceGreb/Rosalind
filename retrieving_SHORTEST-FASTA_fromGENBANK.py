#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:01:55 2023
Given: A collection of n (n≤10

) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.
@author: nikos
"""

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "nikoverg@biol.uoa.gr"
ids=list(input().split())
handle = Entrez.efetch("nucleotide", id = ids, rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
lengths=list()

for i in range(len(records)):
    lengths.append(len(records[i].seq))
for j in range(len(records)):
    if len(records[j].seq) == min(lengths):
        print(records[j].format("fasta")) 




