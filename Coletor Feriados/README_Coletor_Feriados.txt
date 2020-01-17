Versão Python utilizada 3.7.5(necessario python 3.x + para rodar)

Drivers:
ODBC Driver 17 for sql windows(download) (necessario para a biblioteca pyodbc funcionar)

Comandos Terminal:
pip install -r requirements.txt
python setup.py install
pip install pyodbc

Executavel:
Coletor_Feriados

Alterar Anos de coleta:
as variaveis estão localizadas na linhas 21 e 22;
abrir o executavel em uma IDE de python(exemplo anaconda) ou arquivo txt e modificar os dados entre " " abaixo:
    contador_inicio=Data Inicial desejada
    contador_fim=Data final desejada

configuração sql server:

abrir o executavel em uma IDE de python(exemplo anaconda) ou arquivo txt e modificar os dados entre " " abaixo

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server="--nome do seu servidor--";'
                      'Database="--nome do seu database--";'
                      'Trusted_Connection=yes;')

------------------------------------------------------------------------------------------------------------------------------

cursor.execute('''
               INSERT INTO "rota ate a tabela desejada" ("nomes utilizados para a descrição de campo da tabela em ordem")

exemplo utilizado:

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
               INSERT INTO DB.dbo.Banco (Date,Inflacao_meta,Inflacao_acumulada,
                                         Poupanca,Dolar_compra_PTAX,Dolar_venda_PTAX,Dolar_compra,Dolar_venda,
                                         Euro_compra_PTAX,Euro_venda_PTAX,Euro_compa,Euro_venda,Selic_meta,Selic_real)

referencias :

https://docs.microsoft.com/pt-br/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15
https://github.com/leogregianin/bancocentralbrasil#