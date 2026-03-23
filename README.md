# 🚀 API Flask com Python

Projeto simples de API desenvolvido com Flask para praticar conceitos basicos de backend, rotas HTTP e envio de dados em formato JSON.

## 🎯 Objetivo

Este projeto foi criado com foco em aprendizado, para entender como funciona uma API em Python usando Flask.

## ✨ Funcionalidades

- Verificar se a API esta funcionando
- Listar produtos com GET
- Adicionar produtos com POST
- Atualizar produtos com PUT
- Remover produtos com DELETE
- Retornar dados em formato JSON

## 🛠 Tecnologias utilizadas

- Python
- Flask

## 📁 Estrutura do projeto

- `main.py`
- `teste_api.http`
- `.gitignore`

## ▶️ Como executar

1. Abra o projeto no PyCharm
2. Ative o ambiente virtual
3. Instale o Flask com `pip install flask`
4. Execute o arquivo `main.py`

A API sera iniciada em `http://127.0.0.1:5000`

## 🌐 Rotas da API

- `GET /` verifica se a API esta online
- `GET /produtos` lista os produtos
- `POST /produtos` adiciona um produto
- `PUT /produtos/<id>` atualiza um produto existente
- `DELETE /produtos/<id>` remove um produto existente

## 🧪 Exemplos de teste no PowerShell

Adicionar produto:

`Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5000/produtos" -ContentType "application/json" -Body '{"nome":"Monitor","preco":900}'`

Atualizar produto:

`Invoke-RestMethod -Method Put -Uri "http://127.0.0.1:5000/produtos/2" -ContentType "application/json" -Body '{"nome":"Teclado Gamer","preco":180}'`

Remover produto:

`Invoke-RestMethod -Method Delete -Uri "http://127.0.0.1:5000/produtos/1"`

## 📚 Aprendizados praticados

- Criacao de API com Flask
- Uso de rotas HTTP
- Metodos GET, POST, PUT e DELETE
- Manipulacao de JSON
- Testes locais no navegador e PowerShell
- Uso de Git e GitHub

## 🔮 Melhorias futuras

- Validar melhor os dados enviados
- Separar as rotas em arquivos diferentes
- Integrar com banco de dados
- Criar uma interface web para consumir a API
