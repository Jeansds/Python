# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:56:53 2020

@author: U300398
"""
Meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto"
       "Setembro","Outubro","Novembro","Dezembro"]
def Trans(data):
    try:
        print(data[0:2]+" de " + Meses[int(data[3:5])] + " de " + data[6:])
    except:
        print("data invalida")
    
data=input("digite uma data DD/MM/AAAA")
Trans(data)