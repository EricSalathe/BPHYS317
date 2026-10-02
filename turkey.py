#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:20:26 2019

@author: esalathe
"""

f=350. # oven temp
u0=75. # initial room temp
a=1. # radius
k=0.02 # termal difusifity

t = linspace(0,5,10) # time array
u = zeros(10) + f # zteady state temperature with radius

N=5000 

v0 = u0 - f

for i in range(0,N):
    n=i+1
    An = (-1)**(n+1)
    lam = k*n**2*pi**2/a**2
    
    u = u + 2*v0*An*exp(-lam*t)
    
u[0]=u0
    
figure(1)
plot(t,u)


figure(2)   


r = linspace(0,1,20)

for tt in range(0,5+1):
    uu = zeros(20) + f

    for i in range(0,N):
        n=i+1
        uu = uu + \
        2*(u0 - f)*(-1)**(n+1)*exp(-k*n**2*pi**2*tt/a**2)*sin(n*pi*r/a)/(n*pi*r/a)
    
    plot(r,uu)
