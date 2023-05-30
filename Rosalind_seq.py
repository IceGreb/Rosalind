#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:49:08 2023
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s

of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
@author: nikos
"""


word_occs={}
s = input()
for word in list(sorted(set((s)))):
    sum_word=0
    for i in range(len(s)):
        if s[i]==word:
            sum_word+=1
    word_occs[word]=sum_word
for w in word_occs:
    print("{}".format(word_occs[w]), end=' ')
