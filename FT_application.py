#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:24:01 2020

@author: esalathe
"""
from numpy import *
from matplotlib.pyplot import *

x = linspace(0,1.5,100)
y = linspace(0,1.5,100)

z = zeros((size(x),size(y)))

for i in range(size(x)-1):
    for j in range(size(y)-1):
        z[j,i] = 200/pi * (arctan(x[i]/y[j]) - 0.5*arctan((x[i] + 1)/y[j]) - 0.5*arctan((x[i] - 1)/y[j]))

cs=contour(x,y,z, [25, 50, 75])
ylim([0,1])
xlim([0,1.2])
clabel(cs,[25,50,75],fmt='%1.0f')