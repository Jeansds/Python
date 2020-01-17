# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:17:06 2020

@author: U300398, Jean Santos
"""
import requests
import pandas as pd
import pyodbc
import os

Caminho_Arquivo="Chamados BI Total (JIRA - HubCard®).txt"
Tamanho=2000
Chaves=["Chave","Criador","ClienteParceria","Situação","Descrição","Resumo","Last Viewed","Atualizado","Resolvido"]
Descricao={}
Final={}
for i in Chaves:
    Descricao[i]=None
    Final[i]=[]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')        
cursor = conn.cursor()

url='https://jira.hubprepaid.com.br/login.jsp'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
login_data = {
        'os_username': '',
        'os_password': '',
        'os_destination': '/sr/jira.issueviews:searchrequest-excel-all-fields/15675/SearchRequest-15675.xls?tempMax=1000',
        'user_role':'',
        'atl_token':'',
        'login': 'Entrar no Sistema'
        }

j=1
with requests.Session() as c:
    while(j!=0):
        a=c.post(url, data=login_data, headers=headers)
        with open(Caminho_Arquivo,"wb") as f:
            f.write(a.content)
        try:
            arquivo= pd.read_html(Caminho_Arquivo)
            Linhas_Colunas=arquivo[1].shape
            j=0
        except:
            j=j+1
            if(j==6):
                break

for i in range(Linhas_Colunas[0]):
    for j in Chaves:
        if (str(arquivo[1].loc[i,j]))!= "nan" and arquivo[1].loc[i,j]!=" ":
            Descricao[j]=arquivo[1].loc[i,j]
        elif j=="Resolvido" and arquivo[1].loc[i,"Situação"]=="Resolvido":
            if (str(arquivo[1].loc[i,"Atualizado"]))!= "nan":
                Descricao[j]=arquivo[1].loc[i,"Atualizado"]
            else:
                Descricao[j]=arquivo[1].loc[i,"Last Viewed"]
    for j in Chaves:
        if Descricao[j]!=None:
            if(len(Descricao[j]))>Tamanho:
                Descricao[j]=Descricao[j][0:Tamanho]
        Final[j].append(Descricao[j])
        Descricao[j]=None

for i in range(len(Final["Chave"])):
    cursor.execute('''
                   INSERT INTO DB.dbo.Testando(Chamado,Solicitante,Cliente_Relacionado,Resp_BI,Descricao,Resumo,Data_Entrega)
                   VALUES
                   (?,?,?,?,?,?,?)''',Final[Chaves[0]][i],Final[Chaves[1]][i],Final[Chaves[2]][i],Final[Chaves[3]][i],Final[Chaves[4]][i],Final[Chaves[5]][i],Final[Chaves[8]][i])
    conn.commit()

os.remove(Caminho_Arquivo)