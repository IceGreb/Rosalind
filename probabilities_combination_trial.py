#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:18:29 2023

@author: nikos
"""
import numpy as np
import math
a=2
b=2
d=2
n=a+b+d
k=2
#print(n)
c=int(math.factorial(n)/math.factorial(k)*1/math.factorial(n-k))
p_a=(a-1)/c
p_b=(b-1/c)*3/4
p_ab=(a*b)/c
p_ad=(a*d)/c
p_bd=(((b/c)*2)+((d/c)*2))*1/2
p_dom=float(round((p_a)+(p_b)+(p_ab)+(p_ad)+(p_bd),5))
p_dom
#print(c)