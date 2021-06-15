# Projeto Análise de Sentimento em Produção

Este é um projeto para ensino de ciência de dados. O objetivo do projeto é aprender a colocar um modelo preditivo de análise de sentimento em produção. O modelo consiste em um dicionário que contém o peso de cada palavra para tornar uma revisão positiva ou negativa. O função preditiva realiza a predição de um texto em inglês de uma revisão de filme retornando Positivo, Negativo.

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

Diferentes formas de inicializar a aplicação para Windows e Linux:

- No Windows: executando o arquivo `run.py`
```bash
$ python run.py
```

- No Windows: usando o WSGI waitress-serve (disponível no `requirements.txt`, instalado na etapa anterior)
```bash
$ waitress-serve --listen=localhost:8080 app:app
```

- No Linux: executando o arquivo `run.py`
```bash
$ python run.py
```

- No Linux: usando o WSGI gunicorn (disponível no `requirements.txt`, instalado na etapa anterior)
```bash
$ gunicorn app:server
```

Depois de inicializar a aplicação de qualquer uma das formas acessar http://localhost:8080 e testar a aplicação com avaliações em inglês.

## Deploy no Heroku

1. Criar um repositório no seu github a partir deste projeto.
2. Realizar o cadastro/login na plataforma Heroku (https://www.heroku.com/).
3. Criar um novo app e escolher como método de deploy o github. Aqui tem que permitir a autorização do heroku para acessar os projetos de teu github
4. Escolher o projeto que se quer fazer deploy e clicar em deploy.


## Autores

* **Carlos Andres Ferrero** - [anfer86](https://github.com/anfer86)