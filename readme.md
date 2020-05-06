# Projeto Análise de Sentimento em Produção

Este é um projeto para ensino de ciência de dados. O objetivo do projeto é aprender a colocar um modelo preditivo de análise de sentimento em produção. O modelo preditivo realiza a predição de um texto em inglês de uma revisão de filme retornando Positivo, Negativo.

Dividimos a aplicação em duas partes `server-side` e `client-side`. Na pasta `server-side` é realizada a construção do modelo preditivo de análise de sentimento usando Python e também criado um serviço web que escuta uma porta aguardando por requisições de predições usando a biblioteca `Flask`. Na pasta `client-side` montamos uma página com HTML, Bootstrap, JQuery, para que o usuário possa entrar com uma revisão escrita e obter o resultado da predição.

## Pré-requisitos

* Cliente Git (https://git-scm.com). Verifique a instalação digitando:
```bash
$ git --version
```

## Instalação

Clonar o repositório do GitHub.
```bash
$ git clone https://github.com/anfer86/teaching-datascience-sentiment-analysis-model-deploy.git
$ cd teaching-datascience-sentiment-analysis-model-deploy
```

Criar um Virtual Environment para a aplicação. Isto vai criar uma pasta dentro do projeto para colocar as bibliotecas necessárias para rodar a aplicação.
```bash
$ python -m venv env
```

Ativar o Virtual Environment no Windows
```bash
$ env\Scripts\activate.bat
```

Ativar o Virtual Environment no Linux
```bash
$ source env\bin\activate
```

Instalar as dependências presentes no arquivo `requirements.txt`
```bash
$ pip install -r requirements.txt
```

## Utilização

Para rodar a aplicação temos que colocar o servidor escutando uma porta local:
```bash
$ cd server-side
$ python server.py
```

Por fim abrir a página dentro da pasta `client-side` e abrir o arquivo `webpage.html`.

Para testar a aplicação usando Python abrir outro terminal e executar o script de teste:
```bash
$ cd client-side
$ python request.py
```

## Autores

* **Carlos Andres Ferrero** - [anfer86](https://github.com/anfer86)