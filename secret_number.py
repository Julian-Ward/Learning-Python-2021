#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:45:10 2021

@author: julianward
"""

G1 = 0
G2 = 100

print("Please think of a number between 0 and 100!")
guess = 50
ask = 's'



while ask != 'c':
    print("Is your secret number " + str(guess) + "?")
    ask = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if ask in ['h','H']:
        G2 = guess
    if ask == ask in ['l','L']:
        G1 = guess
    if ask in ['c','C']:
        break
    elif ask not in ['h','H','l','L','c','C']:
        print('Sorry, I did not understand your input.')
    guess = int((G1+G2)/2)
    
print('Game over. Your secret number was: ' + str(guess))