# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:26:50 2020

@author: Jean Santos
"""

from lxml import html
import requests
import pyodbc
from datetime import datetime
import re
#from unidecode import unidecode
Fim=datetime.now().year
Inicio=datetime.now().year
Nome_Feriado_Bancario=[]
Data_Feriado_Bancario=[]
Lista_Datas=[]
Lista_Final=[]
Meses={"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
       "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
estado_sigla=[['AC'],['AL'],['AP'],['AM'],['BA'],['CE'],['DF'],['ES'],['GO'],['MA'],['MT'],['MS'],['MG'],['PA'],['PB'],
              ['PR'],['PE'],['PI'],['RJ'],['RN'],['RS'],['RO'],['RR'],['SC'],['SP'],['SE'],['TO']]
#conexao com banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')        
cursor = conn.cursor()
Enviar = '''INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
            VALUES'''
#Inicio do Programa
#Coleta de todos os feriados Estaduais
for Contador in range(len(estado_sigla)):
    contador_inicio=Inicio
    contador_fim=Fim
    while contador_inicio<=contador_fim:
        page = requests.get('http://www.feriados.com.br/feriados-estado-'+estado_sigla[Contador][0]+'.php?ano=' + str(contador_inicio))#aceso ao site que possue os feriados
        tree = html.fromstring(page.content)
        feriados_nomes_municipais = tree.xpath('//span[@class="style_lista_feriados"]//a[@href]/text()')
        feriados_nomes_facultativos = tree.xpath('//span[@class="style_lista_facultativos"]//a[@href]/text()')
        feriados_municipais = tree.xpath('//span[@class="style_lista_feriados"]/text()')
        feriados_facultativos = tree.xpath('//span[@class="style_lista_facultativos"]/text()')
        #junção das arvores
        i=0
        k=0
        while(i<len(feriados_municipais)):
            if  feriados_municipais[i][-3::] == ' - ':
                feriados_municipais[i]= feriados_municipais[i]+feriados_nomes_municipais[k]
                k=k+1
            i=i+1
        i=0
        k=0
        while(i<len(feriados_facultativos)):
            if  feriados_facultativos[i][-3::] == ' - ':
                feriados_facultativos[i]= feriados_facultativos[i]+feriados_nomes_facultativos[k]
                k=k+1;
            i=i+1
            
        for i in range(len(feriados_facultativos)):
            a=feriados_facultativos[i].split(" - ")
            Lista_Datas.append(a[0])
            estado_sigla[Contador].append([a[0],a[1],"Sim"])
        for i in range(len(feriados_municipais)):
            a=feriados_municipais[i].split(" - ")
            Lista_Datas.append(a[0])
            estado_sigla[Contador].append([a[0],a[1],"Nao"])
            contador_inicio=contador_inicio+1
    print(Contador)
    Contador=Contador+1
    
contador_inicio=Inicio
contador_fim=Fim
#Coleta de todos os feriados Bancarios Estaduais
while(contador_inicio<=contador_fim):
    page = requests.get('https://feriadosbancarios.febraban.org.br/feriados.asp?ano='+str(contador_inicio))
    tree = html.fromstring(page.content)
    Leitor=tree.xpath('//table//table//text()')

    for j in range(len(Leitor)):
        k=Leitor[j].replace(" ","")
        if re.search('[0-9]',k[0:1]):
            if k[8:11] in Meses:
                Data_Feriado_Bancario.append(k[0:2] +"/"+ Meses[k[8:11]] +"/"+ str(contador_inicio))
                Nome_Feriado_Bancario.append(Leitor[j+4])
    contador_inicio=contador_inicio+1
#envia as datas que não são feriados comuns porem são bancarios
for i in range(len(Data_Feriado_Bancario)):
    if Lista_Datas.count(Data_Feriado_Bancario[i])<=26:
        cursor.execute('''
                       INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                       VALUES
                       (?,?,'Sim','Nacional','Sim')''',datetime.strptime(Data_Feriado_Bancario[i],'%d/%m/%Y'),Nome_Feriado_Bancario[i])
        conn.commit()
#Envio ao banco de dados todos os feriados Estaduais os classificando antes do envio      
for i in range(len(estado_sigla)):
    j=1
    while(j<(len(estado_sigla[i]))):
        Contador_Data=Lista_Datas.count(estado_sigla[i][j][0])
        Contador_Data_Bancaria=Data_Feriado_Bancario.count(estado_sigla[i][j][0])
        Re=estado_sigla[i][j][0] + estado_sigla[i][0]
        Contador_Lista_Final=Lista_Final.count(Re)
        if Lista_Final.count(estado_sigla[i][j][0] + "Nacional")==0:
            if Contador_Data>=26 and Contador_Data_Bancaria!=0:
                cursor.execute(Enviar + '''(?,?,?,'Nacional','Sim')''',datetime.strptime(estado_sigla[i][j][0],'%d/%m/%Y'),estado_sigla[i][j][1],estado_sigla[i][j][2])
                conn.commit()
                Lista_Final.append(estado_sigla[i][j][0] + "Nacional")
                
            elif Contador_Data>=26 and Contador_Data_Bancaria==0:
                cursor.execute(Enviar + '''(?,?,?,'Nacional','Nao')''',datetime.strptime(estado_sigla[i][j][0],'%d/%m/%Y'),estado_sigla[i][j][1],estado_sigla[i][j][2])
                conn.commit()
                Lista_Final.append(estado_sigla[i][j][0] + "Nacional")
                    
            elif Contador_Lista_Final==0 and Contador_Data_Bancaria!=0:
                cursor.execute(Enviar + '''(?,?,?,?,'Sim')''',datetime.strptime(estado_sigla[i][j][0],'%d/%m/%Y'),estado_sigla[i][j][1],estado_sigla[i][j][2],estado_sigla[i][0])
                conn.commit()
                Lista_Final.append(Re)
                
            elif Contador_Lista_Final==0 and Contador_Data_Bancaria==0:
                cursor.execute(Enviar + '''(?,?,?,?,'Nao')''',datetime.strptime(estado_sigla[i][j][0],'%d/%m/%Y'),estado_sigla[i][j][1],estado_sigla[i][j][2],estado_sigla[i][0])
                conn.commit()
                Lista_Final.append(Re)
        j=j+1