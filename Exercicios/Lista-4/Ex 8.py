# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:11:20 2020

@author: U300398
"""
import random
Dicionario={"A":["4","@","/\\", "/-\\", "^", "ä", "ª", "aye"],"B":["8", "6", "|3", "ß", "P>", "|:"],"C":["[","¢", "<", "("]," ":[" "],
            "D":["|))","o|","[)","I>","|>","?"],"E":["3","&","£","ë","[-","€","ê","|=-"],"F":["|=","ph","|#"],"G":["6","&","(_+","9","C-","gee","(,"],
            "H":["#","/-/","[-]","{=}","<~>","|-|","]~[","}{","]-[","?","8", "}-{"],"I":["1","!","|","&","eye","3y3","ï","][","[]"],
            "J":["j",";","_/","</","(/"],"K":["X","|<","|{","]{","}<","|("],"L":["1","7","1_","|","|_","#","¬","£]"],"M":["//.","^^","|v|","[V]",
            "{V}","|\/|","/\\/\\","(u)","[]V[]","(V)","/|\\","IVI"],"N":["//","^/","|\|","/\/","[\]","<\>","{\}","[]\[]","n","/V","₪]"],
            "O":["0","()","?p","*","ö"],"P":["|^","|*","|o","|^(o)","|>","|""","9","[]D","|º","|7"],"Q":["q","9","(_,)","o,"],"R":["|2","P\\","|?",
            "|^","lz","[z","12","Я"],"S":["5","$","z","§","ehs"],"T":["7","+","-|-","1","']['", "\"|\""],"U":["(_)","|_|","v","ü"],"V":["V"],
            "W":["\/\/","vv","'//","\^/","(n)","\V/","\//","\X/","\|/"],"X":["><","Ж","ecks",")("],"Y":["Y","j","`/","¥"],"Z":["2","z","~\_","~/_","%"]}

def Traduzir(Frase):
    try:
        Final=""
        for i in range(len(Frase)):
            Final=Final+str(random.choice(Dicionario[Frase[i]]))
        print(Final)
    except:
        Final=[]
        Possibilidade=[]
        Palavra_Final=[]
        for i in range(len(Frase)):
            j=i+1
            while(j<i+5):
                for k in Dicionario.values():
                    for l in k:
                        if l==Frase[i:j]:
                            Possibilidade.append([str(list(Dicionario.keys())[list(Dicionario.values()).index(k)]),l])
                j=j+1
        print(Possibilidade)
        Primeira=0
        k=0
        while(k<len(Final)+1):
            if(len(Final)>=1):
                Primeira=1
            j=0
            #Contador=0
            while(j<len(Possibilidade)):
                i=0
                while(i<len(Possibilidade)):
                    if Primeira==0:
                        if (Possibilidade[i][1]+Possibilidade[j][1]==Frase[0:len(Possibilidade[i][1]+Possibilidade[j][1])]
                            and Palavra_Final.count(Possibilidade[i][0])==0):
                            Final.append(Possibilidade[i][1])
                            Palavra_Final.append(Possibilidade[i][0])
                            #Contador=1
                            
                    elif (Possibilidade[i][1]+Possibilidade[j][1]==Frase[len(Final[k-1]):len(Possibilidade[i][1]+Possibilidade[j][1]+Final[k-1])]
                        and Palavra_Final.count(Palavra_Final[k-1]+Possibilidade[i][0])==0):
                        #Contador=1
                        Final.append(Final[k-1])
                        Palavra_Final.append(Palavra_Final[k-1])
                        Final[k-1]=Final[k-1]+Possibilidade[i][1]
                        Palavra_Final[k-1]=Palavra_Final[k-1]+Possibilidade[i][0]
                    i=i+1
                j=j+1
            #if Contador==1:
            k=k+1
            #else:
            #    Final.pop(k-1)
            #    Palavra_Final.pop(k-1)
        Resposta=[]
        
        for i in range(len(Final)):
            k=len(Possibilidade)
            while(k!=0):
                if Final[i]+Possibilidade[k-1][1]==Frase and Resposta.count(Palavra_Final[i]+Possibilidade[k-1][0])==0:
                    print(Palavra_Final[i]+Possibilidade[k-1][0])
                    Resposta.append(Palavra_Final[i]+Possibilidade[k-1][0])
                k=k-1
        #*7/\ [V]ë(_) |3()(u)
        #|30/\/\ o||^
        # ö#ª ^^|=-|_| |^@|^[/\
        #0|/\
        #ê174 @<ölz|>ä 4&?p[z^ //.€|_| P>*^^
Traduzir(str(input("Digite uma frase")))