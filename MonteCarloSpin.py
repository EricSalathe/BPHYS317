#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:31:56 2020

@author: esalathe
"""
import random

Nexp = 200
Natom = 10000

Mav = 0
Mtyp = 0

for exp in range(Nexp):
    M = 0   
    for i in range(Natom):
        s = random.randint(0,1)*2 - 1
        M = M + s
    
    Mav = Mav

#    print(M)
    
Mav=Mav/Nexp

print('Average Value=',Mav)
print('Typical Value=',sqrt(Natom))
    