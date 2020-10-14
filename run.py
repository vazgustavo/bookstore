from flask import Flask, jsonify, request
from Include.Book import Book
from Include.Client import Client
import json

app = Flask(__name__)


def checkDelay(valor, dias):
    if dias > 2:
        return valor + 0.3 + (dias * 0.2)
    elif dias > 3:
        return valor + 0.5 + (dias * 0.4)
    elif dias > 5:
        return valor + 0.7 + (dias * 0.6)
    else:
        return valor


book = Book(0, 'livre pra recomecar', 'romance', True, 2, 10, 0, 0)
book1 = Book(1, 'viajantes do tempo', 'aventura', False, 3, 10, 0, 0)
book2 = Book(2, 'o nome do tempo', 'aventura', False, 4, 13, 0, 3)
book3 = Book(3, 'a medicina dos horrores', 'terror', False, 5, 17, 0, 1)
book4 = Book(4, 'intensa paixao', 'romance', False, 7, 22, 0, 0)

client = Client(0, 'gustavo', 'vaz', '01410752095', 4)
client1 = Client(1, 'rogerio', 'silveira', '09863424536', 3)
client2 = Client(2, 'rodrigo', 'antunes', '09863424536', 2)

books = [book, book1, book2, book3, book4]
clients = [client, client1, client2]


@app.route('/client/<int:id_cliente>/books')
def returnBooksIdClient(id_cliente):
    for i in range(len(books)):
        if books[i].idCliente == id_cliente:
            books[i].total = checkDelay(books[i].valor, books[i].diasEmAtraso)
            return json.dumps(books[i], default=lambda x: x.__dict__)


@app.route('/books/<int:id>/reserve', methods=['GET'])
def reserveBook(id):
    books[id].disponibilidade = False
    response = {'status': 'alterado', 'mensagem': 'livro reservado com sucesso'}
    return jsonify(response)


@app.route('/books')
def returnAllBooks():
    return json.dumps(books, default=lambda x: x.__dict__)


if __name__ == '__main__':
    app.run(debug=True)
