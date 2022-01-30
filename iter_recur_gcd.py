#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:57:36 2021

@author: julianward
"""

def gcdIter(a, b):
    if a>=b:
        test = a
    else:
        test = b
    for i in range(test,1,-1):
        if a%test==0 and b%test == 0:
            break
        else:
            test -= 1
    return test

print(gcdIter(125,25))
        
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
    
print(gcdRecur(51,18))
