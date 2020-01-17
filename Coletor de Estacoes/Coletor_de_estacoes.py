# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:45:01 2019

@author: U300398
"""
from lxml import html
import requests
import pyodbc
Mes=[]
Ano=[]
Estacao=[]
Nome=[]
Meses={"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
       "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
page = requests.get('https://www.iag.usp.br/astronomia/inicio-das-estacoes-do-ano')#aceso ao site que possue os feriados
tree = html.fromstring(page.content)#coleta a arvore do site html
a=tree.xpath('//thead/tr/td//text()')#Coleta da tabela
b=tree.xpath('//thead/tr/th//text()')#Coleta da tabela
for i in b:
    r = i.replace(u'\xa0', u'')
    if r[0:3].lower() in Meses and r[3:4]==" ":
        Mes.append(Meses[i[0:3].lower()])#Meses das Estações
    elif r[0:2]=='20':
        Ano.append(r[0:4])#Anos das Estações
    else:
        Nome.append(i)#Nomes das Estações
Nome.pop(0)
for i in a:
    r = i.replace(u'\xa0', u'')
    r = r.replace(u' ', u'')
    Mes.append(Mes[0])
    Estacao.append(r[0:2] + "-" + Mes.pop(0) + "-" + Ano[0] + " " + r[2:4] + ":" + r[4:6])#Coleta do dia,hora e minutos
    if int(Mes[3])>int(Mes[0]):
        Ano.pop(0) 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')  
cursor = conn.cursor()
for i in Estacao:
    Nome.append(Nome[0])
    cursor.execute('''
                   INSERT INTO DB.dbo.Teste_Estacoes(Estacao,Data)
                   VALUES
                   (?,?)''',Nome.pop(0),i)
    conn.commit()