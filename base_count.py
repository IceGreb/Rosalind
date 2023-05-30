#!/home/nikos/miniconda3/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:43:35 2023

@author: nikos
"""

from Bio.Seq import Seq
sample_seq=Seq(input())
print(sample_seq.count("A"),sample_seq.count("C"),sample_seq.count("G"),sample_seq.count("T"))
