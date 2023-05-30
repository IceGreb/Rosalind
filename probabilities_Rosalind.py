#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 22:28:29 2023
Given: Three positive integers k, m, and n, 
representing a population containing k+m+n organisms: 
    k individuals are homozygous dominant for a factor, 
    m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms 
will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype).
 Assume that any two organisms can mate.
@author: nikos
"""
a=20
b=18
c=26
n=a+b+c
p_a=(a/n)*((a-1)/(n-1))
p_b=(b/n)*((b-1)/(n-1))*0.75
p_ab=((b/n)*(a/(n-1)))+((b/n)*(a/(n-1)))
p_ac=((c/n)*(a/(n-1)))+((c/n)*(a/(n-1)))
p_bc=(((b/n)*(c/(n-1)))+((b/n)*(c/(n-1))))*0.5
p_dominant=float(round((p_a+p_b+p_ab+p_ac+p_bc),5))
p_dominant