# API de Gerenciamento de Contatos

Este projeto é uma API simples construída com **Flask** para gerenciamento de contatos. Ele permite realizar operações básicas de CRUD (Create, Read, Update e Delete) em uma lista de contatos.

## Funcionalidades 🧭

- **GET** `/contato` – Retorna todos os contatos.
- **GET** `/contato/{id}` – Retorna um contato específico, baseado no ID.
- - **GET** `/contato/{nome}` – Retorna um contato específico, baseado no Nome.
- **POST** `/contato` – Cria um novo contato.
- **PUT** `/contato/{id}` – Atualiza um contato existente.
- **DELETE** `/contato/{id}` – Exclui um contato pelo ID.

## Requisitos

- Python 3.13 ou superior
- Flask
- Flask-SQLAlchemy
- Poetry

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/api-gerenciamento-contatos.git

2. No terminal digite os seguintes comandos, em sequência:
    ```
    pip install -r requirements.txt  [serve para instalar todas dependencias do projeto]

    cd src [acessa o diretorio para rodar o código]

    poetry env activate [ ativa ambiente virtual separado dos arquivos da sua maquina, evitando conflitos]

3. No terminal digite "**python app.py**".
    
  
