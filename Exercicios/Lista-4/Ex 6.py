# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:43:58 2020

@author: U300398
"""
Cont=0
Numero=input("digite um numero")
if Numero.count("-"):
    Cont=Cont+1      
if (len(Numero)-Cont)==7:
    Numero="3"+Numero
if Cont==0:
    A=Numero[4:]
    B=Numero[0:4]
    Numero=B+"-"+A
print(Numero)