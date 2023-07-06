from flask import Flask, jsonify, request

servidor = Flask(__name__)

clientes = [{
    "id": 1,
    "nome": "Bob"
},{
    "id": 2,
    "nome": "Pedro"
},{
    "id": 3,
    "nome": "Flavia"
}]

@servidor.route("/", methods=["GET"])
def hello_world():
    return "Olá mundo"

@servidor.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes),200

@servidor.route("/cliente/<int:cliente_id>", methods=["GET"])
def get_cliente_por_id(cliente_id):
    # cliente_encontrado = None
    
    # for cliente in clientes:
    #     if cliente["id"] == cliente_id:
    #         cliente_encontrado = cliente
    cliente = next((cliente for cliente in clientes if cliente["id"] == cliente_id), None)
    if cliente:
        return jsonify(cliente)
    
    return jsonify({"mensagem": "cliente não encontrado"}),404

@servidor.route("/cliente", methods=["POST"])
def criar_cliente():
    novo_nome = request.json["nome"]

    cliente_encontrado = next((cliente for cliente in clientes if cliente["nome"] == novo_nome), None)

    if cliente_encontrado:
        return jsonify({"mensagem": "cliente já cadastrado"}),200
    
    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": request.json["nome"]
    }

    clientes.append(novo_cliente)

    return jsonify(novo_cliente),201

@servidor.route("/cliente/<int:cliente_id>", methods=["DELETE"])
def deletar_cliente_por_id(cliente_id):
    cliente_encontrado = next((cliente for cliente in clientes if cliente["id"] == cliente_id), None)
    
    if cliente_encontrado:
        clientes.remove(cliente_encontrado)
        return jsonify({"mensagem": "cliente deletado", "cliente": cliente_encontrado})
    
    return jsonify({"mensagem": "cliente não encontrado"}),404

@servidor.route("/cliente/<int:cliente_id>", methods=["PUT"])
def atualizar_cliente_por_id(cliente_id):
    cliente_encontrado = next((cliente for cliente in clientes if cliente["id"] == cliente_id), None)
    
    if cliente_encontrado:
        cliente_encontrado['nome'] = request.json["nome"]
        return jsonify({"mensagem": "cliente alterado com sucesso", "cliente": cliente_encontrado})
    
    return jsonify({"mensagem": "cliente não encontrado"}),404

if __name__ == "__main__":
    servidor.run(debug=True, port=8000)