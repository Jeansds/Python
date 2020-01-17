# -*- coding: utf-8 -*-
import requests
from datetime import datetime,timedelta
import pandas as pd
k=[]
l=[]
Contador=0
Escrever=pd.ExcelWriter('Moedas.xlsx', engine='xlsxwriter')
Codigos=["115","61","156","99"]
#Formato de data = DD/MM/YYYY
Inicio=datetime.strftime(datetime.strptime(str(datetime.now().date()-timedelta(days=1)),'%Y-%m-%d'),'%d/%m/%Y')
Fim=datetime.strftime(datetime.strptime(str(datetime.now().date()),'%Y-%m-%d'),'%d/%m/%Y')
for i in Codigos:
    page = requests.get('https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda='+i+'&DATAINI='+Inicio+'&DATAFIM='+Fim)
    k=page.text.split("\n")
    for i in range(len(k)-1):
        l=k[i].split(";")
        l[0]=datetime.strptime(l[0],'%d%m%Y').date()
        for j in range(len(l)):
            Data_Frame=pd.DataFrame({'':[l[j]]})
            Data_Frame.to_excel(Escrever, sheet_name='Sheet1',
            startrow=Contador, startcol=j, header=False, index=False)
        Contador=Contador+1
Escrever.save()