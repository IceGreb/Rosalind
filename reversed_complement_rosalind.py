#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:38:09 2023

@author: nikos
"""

s=input()

t=s.replace("A", '%temp').replace("T", "A").replace('%temp', "T").replace("G",'%temp').replace("C","G").replace("%temp", "C")
complementary_s=t[::-1]
complementary_s