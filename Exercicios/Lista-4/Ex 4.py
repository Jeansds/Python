# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:16:54 2020

@author: U300398
"""
import sys

def Construir(altura,largura):
    if largura>20:
        largura=20
    elif largura<1:
        largura=1
    if altura>20:
        altura=20
    elif altura<1:
        altura=1
    for j in range(altura):
        for i in range(largura):
            if i==j==0 or (i==largura-1 and j==altura-1) or (i==0 and j==altura-1) or (j==0 and i==largura-1):
                sys.stdout.write("+")
            elif i==0 or i==largura-1:
                sys.stdout.write("|")
            elif j==0 or j==altura-1:
                sys.stdout.write("----")
            else:
                sys.stdout.write("    ")
        print("")
    
i=0
while(i==0):
    altura=int(input("altura"))
    largura=int(input("largura"))
    Construir(altura,largura)