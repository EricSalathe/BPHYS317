#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:22:54 2020

@author: esalathe
"""

n=20

x=array([-10,10])

y1=zeros([2,n])
for n in range(n):
    y1[:,n] =  x + n - 10
plot(x,y2)

y2=zeros([2,n])
for n in range(n):
    y2[:,n] = -1*x + n -10 
    
    
plot(x,y1)
plot(x,y2)