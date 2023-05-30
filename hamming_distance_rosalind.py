#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:01:19 2023
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t
Given: Two DNA strings s
and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)
.
@author: nikos
"""
def hamming_distance(s1,s2):
    
    #s1=''
    #t2=''
    dh=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            dh+=1
    return dh
   
hamming_distance('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT')    