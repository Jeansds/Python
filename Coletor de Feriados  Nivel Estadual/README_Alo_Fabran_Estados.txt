Versão Python utilizada 3.7.5(necessario python 3.x + para rodar)

O Coletor de Feriados estaduais pode coletar qualquer feriado Estadual desde 2001 até o ano atual(dependendo da data pode ser retirado do proximo ano tambem,
conferir a disponibilidade no site da febraban, se colocado até o proximo ano por exemplo ele ira funcionar normalmente porem é possivel dependendo da data que 
nem todos os feriados bancarios foram publicados até a data atual logo ira causar a falta de dados)

Site da Febraban: https://feriadosbancarios.febraban.org.br/feriados.asp

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

Para escolher a data de inicio e fim basta mudar os valores das variaveis Fim e Inicio contidos no começo do programa.

exemplo utilizado no programa:

Fim=datetime.now().year
Inicio=datetime.now().year

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')        
cursor = conn.cursor()
Enviar = '''INSERT INTO DB.dbo.Banco(Data,Nome,Facultativo,Estado,Cidade,Bancario)
        VALUES'''

referencias :

https://docs.microsoft.com/pt-br/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15

https://pypi.org/project/Unidecode/

https://anaconda.org/anaconda/unidecode