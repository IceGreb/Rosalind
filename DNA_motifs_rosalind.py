#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:31:25 2023
Given: Two DNA strings s and t

(each of length at most 1 kbp).

Return: All locations of t
as a substring of s.
@author: nick
"""

s=input()
t=input()
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i:j]==t:
            print(i+1,end=" ")
        
    