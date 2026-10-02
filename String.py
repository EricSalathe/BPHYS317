#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:19:38 2019

@author: esalathe
"""
import time


v=1
l=1
h=0.1


n=1000
T = pi
#t = linspace(0,T,n)

n=100
#x=0.5
x=linspace(0,1,n)


N = 100
figure()

for it in range(0,10):
    t=it*0.1
    print(t)

    y = zeros(n)

    for n in range(1,N+1):
        B = (2*sin(n*pi/4) - sin(n*pi/2))/n**2
        y = y + 8*h/pi**2 * B*sin(n*pi*x/l  -  n*pi*v*t/l)/2
    
#plot(t,y)
    time.sleep(0.5)
    plot(x,y)