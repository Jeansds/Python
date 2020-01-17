# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:04:17 2020

@author: U300398
"""

import random
i=0
def randomString(letra):
    return ''.join(random.sample(letra,len(letra)))

while(i==0):
   letra=input("digite uma palava")
   print(randomString(letra))
