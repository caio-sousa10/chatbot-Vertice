Chatbot de Perguntas Frequentes

Este é um projeto de chatbot desenvolvido por mim em Python, utilizando a biblioteca Flask para criação de uma interface web, com integração de HTML e CSS para o design da página. 
O sistema automatiza respostas para perguntas frequentes de forma eficiente, com foco na melhoria do atendimento e expansão futura.


Tecnologias Utilizadas

Python: Linguagem principal do projeto.

Flask: Framework para criar a aplicação web e servidor.

difflib: Biblioteca para encontrar correspondências aproximadas entre perguntas e respostas.

HTML: Linguagem para estruturação da interface web.

CSS: Utilizado para o estilo e design da interface web.


Funcionalidades

Automação de respostas: O chatbot responde automaticamente a perguntas frequentes usando um banco de dados de perguntas e respostas armazenado em dicionários.

Interface web: A aplicação é acessível via navegador, com uma interface simples e funcional.

Expansão futura: O sistema está preparado para futuras melhorias, incluindo integração com outras plataformas ou interfaces.


Estrutura do Projeto

app.py: Código principal do servidor Flask.

chatbot.py: Código da parte lógica do chatbot.

templates/: Contém os arquivos HTML para a interface web.

static/: Contém arquivos CSS e outros recursos estáticos/estilos.


Como utilizar:


Pré-requisitos

Antes de começar, certifique-se de que o seguinte está instalado no seu sistema:

Python (versão 3.x)
As seguintes bibliotecas Python:
Flask
difflib (nativa do Python)
threading


Instalação


Clone o repositório do projeto
Navegue até o diretório do projeto

Instale manualmente (digitando no terminal) as dependências (caso necessário): 
pip install flask 

Executando o Chatbot


Inicie o servidor Flask no terminal: 

python app.py

Abra o navegador e acesse: 

http://localhost:5000


Usando o Chatbot


Na página inicial, você verá um campo para enviar suas perguntas.
Digite sua pergunta e clique em "Enviar".
O chatbot responderá com base no banco de dados(dicionário) de perguntas e respostas configurado no código.
