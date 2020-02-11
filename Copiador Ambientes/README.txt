Versão Python utilizada 3.7.5(necessario python 3.x + para rodar)

Softwares Externos:
Selenium web service
Biblioteca re
Biblioteca Tkinter
MicrosoftWebDriver(Edge)

Observações: 
Para o programa rodar é necessario abrir a barra de pesquisa do seu computador e digitar UAC(Alterar configurações de controle de usuario)
e difinir o nivel de notificações para sempre notificar(3º ou 4º barra de baixo para cima) pois sem isso não é possivel abrir o WebDriver pelo python;

O MicrosoftWebDriver(Edge) precisa ser baixado na sua versão do edge, para verificar a sua versão abra o edge, click em ... e desça até o final das configurações e la havera a sua versão do edge, depois basta entrar no link abaixo e baixar o driver correspondente a sua versão:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

No programa existem variaveis chamadas Base e empresa, a variavel Base é a empresa que servira para fazer a copia do ambiente e a variave Empresa é a empresa de destino que voce deseja criar o portal, coloque o nome exatamente como esta no site pois não ira acessar se estiver incorreto nome(inclui letras maiusculas e minusculas tambem), a Variavel Caminho indica o caminho que seu internet explorer esta baixando os arquivos pois os relatorios serão baixados nesse caminho, copie exatamente o caminho para a sua pasta de download ou a pasta que seu microsoft edge esta fazendo o download(caso não saiba onde seu edge esta fazendo o download nas intruções abaixo voce vera o caminho de download e como alteralo)
Obs: alterar todos os \ por / e adicionar o / no final do caminho pois o programa não ira funcionar se apenas copiar o caminho.

No Edge é necessario configurar os downloads para não precisarem de confirmação quando for solicitado o download, para isso clique em ... no canto superior direito, Configurações avançadas e em Downloads logo abaixo tem a opção: Perguntar o que fazer com cada download, desmarque esta opção.
