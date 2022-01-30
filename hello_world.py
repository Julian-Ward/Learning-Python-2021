#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:20:55 2021

@author: julianward

Inputs: a random string
Outputs: the longest string of alphabetically ordered letters (not necessarily consecutive)

limits/improvements to make: does not work for capital letters, numbers, spaces, 
                             or punctuation within the input string.
"""

s = 'testingatheoryabcdekbabcabcdefk'

scan = 0
longstring = s[0]
alpha = 'abcdefghijklmnopqrstuvwxyz'

while scan < len(s)-1:
    
    charcheck = s[scan]
    val1 = 0
    val2 = 0
    charstring = charcheck
    i = 1
    
    while val1<=val2 and val2 <len(alpha)-1 and (scan+i) < len(s):
        
        "Checks the position of a letter (1st) from the input string in the alphabet"
        "if the letter is not found at a lower ranking in the alphabet"
        "break the string construction"
        while alpha[val1] != charcheck and val1 <len(alpha)-1:
            val1+=1
        if val1 == len(alpha):
            break
        
        "Begin searching downstream from a reference letter (above)"
        nextcheck = s[scan+i]
        val2 = 0
        while alpha[val2] != nextcheck and val2 <len(alpha)-1:
            val2+=1
        "if the next (2nd) letter from reference letter is of lower or equal ranking"
        "to the reference letter, add the next letter to the trial string,"
        "and move index to the next (3rd) letter in the input string."  
        "begin comparing the (2nd) and (3rd) letter as (1st) and (2nd) were compared"
        if val1<=val2 and i+scan < len(s):
            
            charstring = charstring+nextcheck
            charcheck = nextcheck
            i+=1
        "if the (2nd) letter is at the end of the input string, break the search loop"    
        else:
            break
    "after making each trial string from the input string, compare to the existing"
    "longest string and replace if necessary"
    if len(charstring) > len(longstring):
        longstring = charstring
    scan+=1
    
print(longstring)
    
            
            