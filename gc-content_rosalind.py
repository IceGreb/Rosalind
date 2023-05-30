#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:34:03 2023

@author: nikos
"""

def GC(file):
    f=open(file,"r")
    sum_gc=0
    seqs=[]
    
    for i in f:
        ID=f.readline()
        seqs.append(i.rstrip())    
    sequence="".join([base for base in seqs])
    for b in sequence:
        if b == 'G' or b == 'C':
            sum_gc+=1
    print(ID.strip(">\n"))
    print("%.6f"%(sum_gc/len(sequence)*100))

GC("/home/nikos/Λήψεις/rosalind_revc.txt")