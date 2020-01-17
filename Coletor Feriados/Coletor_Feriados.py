from lxml import html
import requests
import pyodbc
from datetime import datetime
import re
#variaveis
Lista_Datas=[]
Lista_Datas_solo=[]
Lista_Feriados=[]
Lista_Nome=[]
Lista_Facultativo=[]
Lista_Final=[]
Nome_Feriado_Bancario=[]
Data_Feriado_Bancario=[]
Temp_1=0
Meses={"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
       "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
estado_sigla=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB',
              'PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
estado_nome=['Acre','Alagoas','Amapa','Amazonas','Bahia','Ceara','Distrito Federal','Espirito Santo','Goias',
        'Maranhao','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Para','Paraiba','Parana',
        'Pernambuco','Piaui','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondonia','Roraima',
        'Santa Catarina','Sao Paulo','Sergipe','Tocantins']
Meses={"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
       "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
for _ in range(len(estado_sigla)):
    contador_inicio=2020
    contador_fim=2020
    while(contador_inicio<=contador_fim):
        page = requests.get('http://www.feriados.com.br/feriados-estado-'+estado_sigla[Temp_1]+'.php?ano=' + str(contador_inicio))#aceso ao site que possue os feriados
        tree = html.fromstring(page.content)#coleta a arvore do site html
        #rastreamento dos objetos nas raizes
        feriados_nomes_municipais = tree.xpath('//span[@class="style_lista_feriados"]//a[@href]/text()')
        feriados_nomes_facultativos = tree.xpath('//span[@class="style_lista_facultativos"]//a[@href]/text()')
        feriados_municipais = tree.xpath('//span[@class="style_lista_feriados"]/text()')
        feriados_facultativos = tree.xpath('//span[@class="style_lista_facultativos"]/text()')
        Cidade=re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]',"",str(tree.xpath('//*[@id="location_header"]/a[2]/text()')))
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
        #tratamentos de repeticao
        for i in feriados_municipais:
            for k in feriados_facultativos:
                if k==i:
                    feriados_municipais.remove(k)
        
        for i in range(len(feriados_municipais)):
            for k in range(len(feriados_municipais)):
                if k!=i and feriados_municipais[k].lower()==feriados_municipais[i].lower():
                    feriados_municipais.remove(i)
                    
        for i in range(len(feriados_facultativos)):
            for k in range(len(feriados_facultativos)):
                if k!=i and feriados_facultativos[k].lower()==feriados_facultativos[i].lower():
                    feriados_facultativos.remove(i)
        #conexao com banco de dados
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=VPD1TEC-001599\MSSQLSERVER01;'
                              'Database=DB;'
                              'Trusted_Connection=yes;')
        
        cursor = conn.cursor()
        #separacao dos dados
        for i in range(len(feriados_facultativos)):
            a=feriados_facultativos[i].split(" - ")
            if Lista_Datas.count(a[0])==0:
                Lista_Datas_solo.append(a[0])
            Lista_Datas.append(a[0])
            Lista_Nome.append(estado_nome[Temp_1])
            Lista_Feriados.append(a[1])
            Lista_Facultativo.append("Sim")
        for i in range(len(feriados_municipais)):
            a=feriados_municipais[i].split(" - ")
            if Lista_Datas.count(a[0])==0:
                Lista_Datas_solo.append(a[0])
            Lista_Datas.append(a[0])
            Lista_Nome.append(estado_nome[Temp_1])
            Lista_Feriados.append(a[1])
            Lista_Facultativo.append("Nao")
            
        contador_inicio=contador_inicio+1;
    #end while
    Temp_1=Temp_1+1
#end for
    
#inicio coleta feriados bancarios    
contador_inicio=2020
contador_fim=2020
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
#commit dos feriados bancarios para o banco de dados
for i in range(len(Data_Feriado_Bancario)):
    if Lista_Datas.count(Data_Feriado_Bancario[i])<=26:
        cursor.execute('''
                       INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                       VALUES
                       (?,?,'Sim','Nacional','Sim')''',datetime.strptime(Data_Feriado_Bancario[i],'%d/%m/%Y'),Nome_Feriado_Bancario[i])
        conn.commit()
#fim coleta feriados bancarios  
          
for i in range(len(Lista_Datas)):
    Contador_Data=Lista_Datas.count(Lista_Datas[i])
    Contador_Data_Bancaria=Data_Feriado_Bancario.count(Lista_Datas[i])
    Re=Lista_Datas[i] + Lista_Feriados[i] + Lista_Nome[i]#mudei no teste 2
    Contador_Lista_Final=Lista_Final.count(Re)

    if Contador_Lista_Final==0 and Contador_Data_Bancaria!=0:
        cursor.execute('''
                       INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                       VALUES
                       (?,?,?,?,'Sim')''',datetime.strptime(Lista_Datas[i],'%d/%m/%Y'),Lista_Feriados[i],Lista_Facultativo[i],Lista_Nome[i])
        conn.commit()
        Lista_Final.append(Re)
        if Contador_Data>=26 and Lista_Final.count(Lista_Datas[i] + Lista_Feriados[i] + "Nacional")==0:
            cursor.execute('''
                           INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                           VALUES
                           (?,?,?,'Nacional','Sim')''',datetime.strptime(Lista_Datas[i],'%d/%m/%Y'),Lista_Feriados[i],Lista_Facultativo[i])
            conn.commit()
            Lista_Final.append(Lista_Datas[i] + Lista_Feriados[i] + "Nacional")
    elif Contador_Lista_Final==0 and Contador_Data_Bancaria==0:
        cursor.execute('''
                       INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                       VALUES
                       (?,?,?,?,'Nao')''',datetime.strptime(Lista_Datas[i],'%d/%m/%Y'),Lista_Feriados[i],Lista_Facultativo[i],Lista_Nome[i])
        conn.commit()
        Lista_Final.append(Re)
        if Contador_Data>=26 and Lista_Final.count(Lista_Datas[i] + Lista_Feriados[i] + "Nacional")==0:
            cursor.execute('''
                           INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Bancario)
                           VALUES
                           (?,?,?,'Nacional','Nao')''',datetime.strptime(Lista_Datas[i],'%d/%m/%Y'),Lista_Feriados[i],Lista_Facultativo[i])
            conn.commit()
            Lista_Final.append(Lista_Datas[i] + Lista_Feriados[i] + "Nacional")