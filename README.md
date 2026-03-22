# 🚀 API Flask com Python

Projeto simples de API desenvolvido com Flask para praticar conceitos basicos de backend, rotas HTTP e envio de dados em formato JSON.

## 🎯 Objetivo

Este projeto foi criado com foco em aprendizado, para entender como funciona uma API em Python usando Flask.

## ✨ Funcionalidades

- Rota inicial para verificar se a API esta funcionando
- Listagem de produtos com metodo `GET`
- Cadastro de produtos com metodo `POST`
- Retorno de respostas em formato JSON

## 🛠 Tecnologias utilizadas

- Python
- Flask

## 📁 Estrutura do projeto

```text
api-flask-python/
├── main.py
├── teste_api.http
└── .gitignore
▶️ Como executar o projeto
Clone o repositorio ou baixe os arquivos.
Abra o projeto no PyCharm.
Crie ou ative o ambiente virtual.
Instale o Flask com o comando:
pip install flask
Execute o arquivo main.py.
A API sera iniciada em:

http://127.0.0.1:5000
🌐 Rotas disponiveis
GET /
Retorna uma mensagem informando que a API esta funcionando.

Exemplo de resposta:

{
  "mensagem": "API Flask funcionando com sucesso!"
}
GET /produtos
Retorna a lista de produtos cadastrados.

Exemplo de resposta:

[
  {
    "id": 1,
    "nome": "Mouse",
    "preco": 50
  },
  {
    "id": 2,
    "nome": "Teclado",
    "preco": 120
  }
]
POST /produtos
Adiciona um novo produto a lista.

Exemplo de envio:

{
  "nome": "Monitor",
  "preco": 900
}
Exemplo de resposta:

{
  "mensagem": "Produto adicionado com sucesso!",
  "produto": {
    "id": 3,
    "nome": "Monitor",
    "preco": 900
  }
}
🧪 Como testar
Voce pode testar a API de diferentes formas:

Pelo navegador, nas rotas GET
Pelo PowerShell usando Invoke-RestMethod
Pelo arquivo teste_api.http no PyCharm, se sua versao permitir
Exemplo no PowerShell:

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5000/produtos" -ContentType "application/json" -Body '{"nome":"Monitor","preco":900}'


📚 Aprendizados praticados

Criacao de API com Flask
Uso de rotas
Metodos GET e POST
Manipulacao de JSON
Teste de endpoints localmente
Uso de Git e GitHub para versionamento


🔮 Melhorias futuras

Adicionar rotas PUT e DELETE
Validar melhor os dados enviados
Separar as rotas em arquivos diferentes
Integrar com banco de dados
