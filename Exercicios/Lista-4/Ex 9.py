# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:10:40 2020

@author: U300398
"""
import csv
arquivo = open(r'C:\Users\U300398\Desktop\CSV.csv')

linhas = csv.reader(arquivo)
Validos=[]
Invalidos=[]
for linha in linhas:
    for i in linha:
        Elemento=i.split(".")
        if int(Elemento[0])<=126 and int(Elemento[0])>=1 and Elemento[1:4]!=["0","0","0"] and Elemento[1:4]!=["255","255","255"]:
            Validos.append(Elemento)
        elif (int(Elemento[0])>=128 and int(Elemento[0])<=191 and int(Elemento[1])>=0 and int(Elemento[1])<=255 and 
               Elemento[2:4]!=["0","0","0"] and Elemento[2:4]!=["255","255","255"]):
            Validos.append(Elemento)
        elif (int(Elemento[0])>=192 and int(Elemento[0])<=223 and (int(Elemento[0]) and int(Elemento[1]))>=0 and
            (int(Elemento[0]) and int(Elemento[1]))<=225 and int(Elemento[3])>=1 and int(Elemento[3])<=254):
            Validos.append(Elemento)
        else:
            Invalidos.append(Elemento)

escrever=csv.writer(open(r'C:\Users\U300398\Desktop\CSV2.csv','w'),delimiter=' ')
escrever.writerows(Validos)
#escrever.writerows(Invalidos)