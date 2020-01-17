Versão Python utilizada 3.7.5(necessario python 3.x + para rodar)

O Coletor de Chamados Resolvidos tem como intuito entrar no dominio do jira, baixar a query selecionada pelo link no formato html e logo apos as organizar no banco de dados;
A query do link utilizada atualmente pentece a este login e senha logo, não compartilhar este programa com outras pessoas pois possui informações confidencias de acesso;
A query retorna todos os resultados de chamados que tiveram seu status alterado para "Resolvido" nas ultimas 24h.

Sites:https://jira.hubprepaid.com.br/login.jsp

Bibliotecas:
ODBC Driver 17 for sql windows, https://www.microsoft.com/pt-br/download/details.aspx?id=56567
Pandas, https://pandas.pydata.org/pandas-docs/stable/install.html
Request, https://anaconda.org/anaconda/requests

Todos os links possuem os tutoriais para instalação de sua respectiva biblioteca, todas são necessarias para o programa funcionar.

Executavel:
Coletor_Chamados_Resolvidos

O Programa:
No inicio do programa encontramos as variaveis:
Caminho_Arquivo="", necessario colocar o caminho do arquivo em que ele sera salvo ou somente o seu nome e formato, se for colocado um caminho de C: preencher a string com r antes do caminho, Ex: Caminho_Arquivo=r'C:\Users\U300398\Desktop\Chamados BI Total (JIRA - HubCard®).txt';
Tamanho=Int, a variavel tamanho corresponde a quantidade maxima de caracteres que o banco de dados aceita pois existe um limite para cada tipo de variavel, se este limite for ultrapassado o banco de dados ira dar o erro de truncate e parar a execução;
Chaves=[""], Nome de todos so campos na tabela que são lidos, se caso for necessario adicionar ou retirar um campo das Chaves lembrar de alterar o INSERT no final do programa para corresponder corretamente os campos e seus preenchimentos;

Conexão Banco de Dados:

Como no exemplo logo a abaixo o programa se liga ao banco de dados atraves da biblioteca pyodbc, é necessario alterar o Servidor e Database para o seu correspondente no banco de dados atual para encontrar a tabela de destino:

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VPD1TEC-001599\MSSQLSERVER01;'
                      'Database=DB;'
                      'Trusted_Connection=yes;')        
cursor = conn.cursor()

No Final do programa é possivel encontrar o insert do banco de dados, necessario alterar os campos para os correspondentes da sua tabela, lembrando que os numeros das variaveis Final[Chaves[Int]][i] correspondem a posição delas na Lista Chaves=[""](Listas tem a contagem iniciada em 0).

cursor.execute('''
               INSERT INTO DB.dbo.Testando(Chamado,Solicitante,Cliente_Relacionado,Resp_BI,Descricao,Resumo,Data_Entrega)
               VALUES
              (?,?,?,?,?,?,?)''',Final[Chaves[0]][i],Final[Chaves[1]][i],Final[Chaves[2]][i],Final[Chaves[3]][i],Final[Chaves[4]][i],Final[Chaves[5]][i],Final[Chaves[8]][i])
conn.commit()

Query:
Se for necessario alterar a query é possivel realiza-la no site do jira sem alterar o programa basta salvar no mesmo espaço da query existente que o link ira se manter.

Referencias:

https://pandas.pydata.org/pandas-docs/version/0.23/;

https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html;

https://github.com/mkleehammer/pyodbc/wiki.