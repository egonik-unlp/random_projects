#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:01:43 2021

@author: gonik
"""

def no_se_que_hace(N):
    nr=0
    for i in range(N):
        x=np.random.random() #0 y 1 con distribucion uniforme 
        y=np.random.random() #0 y 1 con distribucion uniforme 
        r=np.sqrt(x**2 + y**2)
        if r < 1:
            nr+=1
    return (nr/N)*4


    
print(no_se_que_hace(1000000))