#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:46:36 2021

@author: julianward
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    prod = 1
    for i in range(exp):
        prod = prod*base
    return prod
print(iterPower(3, 5))
        