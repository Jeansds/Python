# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:43:08 2020

@author: U300398
"""

import pandas as pd
import re

Arquivo= open(r'C:\Users\U300398\Desktop\Exercicio.txt')
Usuario=[]
Bytes=[]
Espaco_Utilizado=[]
Porcentagem=[]

def ler():
    for i in Arquivo.readlines():
        #print(i.split("\n"))
        i=re.sub("\n","",i)
        i=i.split()
        Usuario.append(i[0])
        Bytes.append(i[1])
        
def Calcular(Bytes):
    Soma=0
    for i in Bytes:
        Mb=(float(i)/1024)/1024
        Espaco_Utilizado.append(round(Mb,2))
        Soma=Soma+round(Mb,2)
    for i in Espaco_Utilizado:
        Porcentagem.append(round(i/Soma*100,2))

def Escrever():
    A=open(r'C:\Users\U300398\Desktop\Exercicio.txt','a')
    A.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    A.write('------------------------------------------------------------------------\n')
    A.write('Nr,Usuário,Espaço utilizado,% do uso\n')
    for i in range(len(Usuario)):
        A.write(str(i+1)+","+Usuario[i]+","+str(Espaco_Utilizado[i])+" MB,"+str(Porcentagem)+"% \n")
ler()
Calcular(Bytes)
Escrever()
print(Porcentagem)