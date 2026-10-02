#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:17:22 2020

@author: esalathe
"""
import random


N = 100

Int = 0
for i in range(N):
   x = random.random()
   Int = Int + x**2
   print(Int/(i+1))
   
Int=Int/N
print(Int)