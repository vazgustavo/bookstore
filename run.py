from flask import Flask, jsonify, request
import json

app = Flask(__name__)

books = [
    {
        'id': 0,
        'nome': 'viajantes do tempo',
        'categoria': 'aventura',
        'disponibilidade': False
    },
    {
        'id': 1,
        'nome': 'o nome do tempo',
        'categoria': 'aventura',
        'disponibilidade': False
    },
    {
        'id': 2,
        'nome': 'a medicina dos horrores',
        'categoria': 'terror',
        'disponibilidade': False
    }
]


@app.route('/books')
def returnBooks():
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def returnBookId(id):
    if request.method == 'GET':
        try:
            response = books[id]
        except IndexError:
            mensagem = 'livro de ID {} não existe!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        response = json.loads(request.data)
        books[id] = response
        return jsonify(response)
    elif request.method == 'DELETE':
        books.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})


@app.route('/books/insert', methods=['POST'])
def insertBook():
    response = json.loads(request.data)
    books.append(response)
    return jsonify({'status': 'created', 'mensagem': 'registro inserido com sucesso!'})


@app.route('/<int:id>')
def livroId(id):
    return jsonify({'id': id, 'nome': 'blue'})


# @app.route('/soma', methods=['POST'])
# def soma():
#     dados = json.loads(request.data)
#     print(dados)
#     total = sum(dados['valores'])
#     return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
