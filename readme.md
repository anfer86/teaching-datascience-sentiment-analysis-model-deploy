# Projeto Análise de Sentimento em Produção

Este é um projeto para ensino de ciência de dados. O objetivo do projeto é aprender a colocar um modelo preditivo de análise de sentimento em produção. O modelo proditivo realiza a predição de um texto em inglês de uma revisão de filme retornando Positivo ou Negativo.

Dividimos a aplicação em duas partes `server-side` e `client-side`. Na pasta `server-side` é realizada a construção do modelo preditivo de análise de sentimento usando Python e também criado um serviço web que escuta uma porta aguardando por requisições de predições usando a biblioteca `Flask`. Na pasta `client-side` montamos uma página com HTML, Bootstrap, JQuery, para que o usuário possa entrar com uma revisão escrita e obter o resultado da predição.

## Pré-requisitos

* Cliente Git (https://git-scm.com). Verifique a instalação digitando:
```bash
$ git --version
```

## Instalação

Clonar o repositório do GitHub e usar o `npm` do Node.js para instalar as dependências do projeto.
```bash
$ git clone https://github.com/anfer86/teaching-datascience-sentiment-analysis-model-deploy.git
$ cd teaching-datascience-sentiment-analysis-model-deploy
```

## Utilização

Para rodar a aplicação temos que colocar o servidor escutando uma porta local:
```bash
$ cd teaching-datascience-sentiment-analysis-model-deploy
$ cd server-side
$ python server.py
```
Pode ser necessária a instalaçao de algumas bibliotecas para colocar esse servidor para rodar. Posteriormente irei colocar um arquivo requirements.txt com essas bibliotecas.

Para testar se esta funcionando corretamente abrir outro terminal e executar o script de teste:
```bash
$ cd teaching-datascience-sentiment-analysis-model-deploy
$ cd client-side
$ python request.py
```

Por fim abrir a página dentro da pasta `client-side` e abrir o arquivo `webpage.html`. 

## Desenvolvimento

O projeto foi desenvolvido com:

* [Sublime Text](https://www.sublimetext.com/) - Editor de texto para programação

## Autores

* **Carlos Andres Ferrero** - [anfer86](https://github.com/anfer86)