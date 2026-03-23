from flask import Flask, jsonify, request

# Inicializa a aplicacao Flask
app = Flask(__name__)

# Lista de produtos em memoria
produtos = [
    {"id": 1, "nome": "Mouse", "preco": 50},
    {"id": 2, "nome": "Teclado", "preco": 120}
]


# Rota inicial para verificar se a API esta funcionando
@app.route("/")
def home():
    return jsonify({"mensagem": "API Flask funcionando com sucesso!"})


# Retorna a lista de produtos cadastrados
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)


# Recebe um novo produto e adiciona na lista
@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    dados = request.get_json()

# Atualiza um produto existente pelo id
@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()

    for produto in produtos:
        if produto['id'] == id:
            produto['nome'] = dados['nome']
            produto['preco'] = dados['preco']

            return jsonify({"mensagem": "Produto atualizado com sucesso!", "produto": produto})
    return jsonify({'mensagem': 'Produto não encontrado!'}),404


# Remove um produto existente pelo id
@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)

            return jsonify({"mensagem": "Produto removido com sucesso!"})

    return jsonify({"mensagem": "Produto nao encontrado"}), 404






    novo_produto = {
        "id": len(produtos) + 1,
        "nome": dados["nome"],
        "preco": dados["preco"]
    }

    produtos.append(novo_produto)

    return jsonify({
        "mensagem": "Produto adicionado com sucesso!",
        "produto": novo_produto
    }), 201


# Executa o servidor em modo de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)
