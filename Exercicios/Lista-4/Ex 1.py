# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:53:51 2020

@author: U300398
"""
import random
numero=0
def Jogo_de_Craps(a,i,numero):
    if i==0:
        if a==7 or a==11:
            print("voce um natural e ganhou")
            return 1
        elif a==2 or a==3 or a==12:
            print("craps voce perdeu")
            return 1
        else:
            print("voce fez um ponto")
            numero=a
            return numero
    else:
        if a==numero:
            print("voce ganhou em : " + str(i) + " rodadas")
            return 1
        else:
            print("tenta novamente")
            return numero
i=0
while(numero!=1):
    input("aperte enter para rodar")
    a=random.randrange(2,13,1)
    numero=Jogo_de_Craps(a,i,numero)
    i=i+1