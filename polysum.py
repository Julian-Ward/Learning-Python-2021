#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:31:55 2021

imports the math library for trigonometric operations
inputs: n - polygon side number
        s - polygon regular side length
outputs: sum of polygon area and squared perimeter to 4.d.p
"""
from math import *
def polysum(n, s):
    perimeter_sq = (n*s)**2
    area_num = n*s**2
    area_den = 4*tan(pi/n)
    return round(perimeter_sq + area_num/area_den,4)
    


