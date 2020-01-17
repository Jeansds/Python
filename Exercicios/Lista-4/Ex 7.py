# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:59:21 2020

@author: U300398
"""
import random
vetor = ["maca", "laranja", "banana", "cereja"]
palavra=random.choice(vetor)
Vidas=6
i=0
def Jogo(resposta):
    if resposta==palavra:
        print("voce ganhou")
        return 0
    else:
        print("voce errou")
        return 1
    
def randomString(letra):
    return ''.join(random.sample(letra,len(letra)))

Palavra_Embaralhada=randomString(palavra)

while(i==0):
   print(Palavra_Embaralhada)
   Teste=Jogo(input("digite a palavra"))
   if Teste==0:
       print("sobraram "+str(Vidas)+" Vidas")
       print("a palavra é : "+palavra)
       i=1
   else:
       Vidas=Vidas-Teste
       print("Vidas Restantes: "+ str(Vidas))