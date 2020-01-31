import requests
from datetime import datetime,timedelta
import pandas as pd
from tkinter import *
import operator
import xlsxwriter
import re

def quit():
    global root
    window.quit()
def get(l1):
	global Dia
	global Mes
	global Ano
	Dia=e1.get()
	Mes=e2.get()
	Ano=e3.get()
	l1.destroy()
	l1=Label(window,text="Data: "+Dia+"/"+Mes+"/"+Ano)
	l1.grid(row=5,column=1)
def download(l1):
	k=[]
	l=[]
	Final=[]
	Contador=1
	Codigos=["115","61","156","99","222"]
	Cabec=["Data","Sigla","Compra(Pariedade BRL)","Venda(Pariedade BRL)","Compra(Pariedade USD)","Venda(Pariedade USD)"]
	#Formato de data = "DD/MM/YYYY"
	Inicio=Dia+"/"+Mes+"/"+Ano
	Fim=datetime.strftime(datetime.strptime(str(datetime.now().date()),'%Y-%m-%d'),'%d/%m/%Y')
	Nome=re.sub("-","",str(datetime.now().date()))+'_BC cotacao.xlsx'
	Escrever=pd.ExcelWriter(Nome, engine='xlsxwriter')
	for i in range(6):
		Data_Frame=pd.DataFrame({'':[Cabec[i]]})
		Data_Frame.to_excel(Escrever, sheet_name='Sheet1',startrow=0,
                        	startcol=i, header=False, index=False)
	l1.destroy()
	l1=Label(window,text="Realizando Download")
	l1.grid(row=5,column=1)
	for i in Codigos:
		try:
			page = requests.get('https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda='+i+'&DATAINI='+Inicio+'&DATAFIM='+Fim)
			k=page.text.split("\n")
			for j in k:
				l=j.split(";")
				l[0]=l[0][0:2]+"/"+l[0][2:4]+"/"+l[0][4:]
				if l!=[''] and l!=['//']:
					Final.append(l)
		except:
			pass
	print(Final)
	Final=sorted(Final,key=operator.itemgetter(0))
	for i in Final:
		for j in range(len(i)):
			Data_Frame=pd.DataFrame({'':[i[j]]})
			Data_Frame.to_excel(Escrever, sheet_name='Sheet1',
								startrow=Contador, startcol=j, header=False, index=False)
		Contador=Contador+1
	Escrever.save()
	l1.destroy()
	l1=Label(window,text="Download Finalizado")
	l1.grid(row=5,column=1)

window=Tk()
l1=Label(window,text="Autor:")
l1.grid(row=0,column=0)
l1=Label(window,text="Jean Santos")
l1.grid(row=1,column=0)
l1=Label(window,text="O Download sera feito da data")
l1.grid(row=0,column=1)
l1=Label(window,text="Informada até a Data Atual")
l1.grid(row=1,column=1)
l1=Label(window,text="Digite o Dia(DD):")
l1.grid(row=2,column=0)
l1=Label(window,text="Digite o Mês(MM):")
l1.grid(row=3,column=0)
l1=Label(window,text="Digite o Ano(AAAA):")
l1.grid(row=4,column=0)
l1=Label(window,text="Status:Esperando Data")
l1.grid(row=5,column=1)

e1=Entry(window)
e1.grid(row=2,column=1)

e2=Entry(window)
e2.grid(row=3,column=1)

e3=Entry(window)
e3.grid(row=4,column=1)

b1=Button(window, text="Enter",command=lambda:get(l1))
b1.grid(row=5,column=0)

b1=Button(window, text="Download",command=lambda:download(l1))
b1.grid(row=6,column=0)

b2=Button(window,text="Quit",command=quit)
b2.grid(row=6,column=1)
window.mainloop()
