#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:03:28 2019

@author: esalathe
"""

A=array([[2,-1],[-1,2]])
print(A)
eig(A)
d,V=eig(A)

V = V*sqrt(2)

print(d)
print(V)


w1=sqrt(d[0])
w2=sqrt(d[1])

g1 = 1
g2 = 1


t=linspace(0,20*2*pi,2000)

x1 = g1*V[0,0]*cos(w1*t) + g2*V[1,0]*cos(w2*t)
x2 = g1*V[0,1]*cos(w1*t) + g2*V[1,1]*cos(w2*t)

print('initial condition: ', x1[0],x2[0])

figure(1)
plot(t,x1,'b', t,x2,'r')

figure(2)
plot(x1,x2)
plot(g1*array([0,V[0,0]]), g1*array([0,V[0,1]]), 'b')
plot(g2*array([0,V[1,0]]), g2*array([0,V[1,1]]), 'r' )
plot(x1[0],x2[0],'r.')