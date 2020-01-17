Versão Python utilizada 3.7.5(necessario python 3.x + para rodar)

O coletor de Feriados Estaduais e Municipais coleta sempre do ano atual em que esta sendo executado, é recomendado sempre executalo em janeiro pois 
a FEBRABAN retira os feriados municipais bancarios de sua lista conforme o tempo passa logo se executado após isto pode criar incoerrencia nos feriados municipais,
conferir o site da febraban para possiveis duvidas das datas disponeveis.

site da febraban:https://feriadosbancarios.febraban.org.br/feriados_show.asp

Drivers:
ODBC Driver 17 for sql windows(download) (necessario para a biblioteca pyodbc funcionar)
Biblioteca Unidecode e Pyodbc tambem são necessarias.

Comandos Terminal:
python setup.py install
pip install pyodbc
pip install unidecode

Executavel:
Alo_Fabran_Estados

configuração sql server:

abrir o executavel em uma IDE de python(exemplo anaconda) ou arquivo txt e modificar os dados entre " " abaixo de todos os campos do arquivo com essa configuração:

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server="--nome do seu servidor--";'
                      'Database="--nome do seu database--";'
                      'Trusted_Connection=yes;')

------------------------------------------------------------------------------------------------------------------------------

Enviar = '''INSERT INTO DB.dbo.Banco("Nomes dos Campos que iram guardar os valores na ordem a baixo")
            VALUES''

exemplo utilizado no programa:

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')        
cursor = conn.cursor()
Enviar = '''INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Cidade,Bancario)
        VALUES'''

Exemplo de Query SQL, no exemplo ira puxar todos os feriados do estado do Acre, substituindo os campos é possivel pegar qualquer outro resultado:

/****** Script for SelectTopNRows command from SSMS  ******/
select * from (SELECT [Data]
      ,[Nome]
      ,[Estado]
      ,[Cidade]
      ,[Facultativo]
      ,[Bancario]
  FROM [DB].[dbo].[Banco]
  where Estado='Nacional' or Estado='AC'
  ) as k where k.cidade is null

OBS:
Provavelmente o programa sera relativamente lento demorando em torno de 15minutos para finalizar toda a execução pois são mais de 6 mil requisições totais a diferentes sites.
referencias :

https://docs.microsoft.com/pt-br/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15

https://pypi.org/project/Unidecode/

https://anaconda.org/anaconda/unidecode