class Book:
    def __init__(self, id, nome, categoria, disponibilidade, diasEmAtraso, valor, total, idCliente):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.disponibilidade = disponibilidade
        self.diasEmAtraso = diasEmAtraso
        self.valor = valor
        self.total = total
        self.idCliente = idCliente

        def setId(self, id):
            self.id = id

        def getId(self):
            return self.id

        def setNome(self, nome):
            self.nome = nome

        def getNome(self):
            return self.nome

        def setCategoria(self, categoria):
            self.categoria = categoria

        def getCategoria(self):
            return self.categoria

        def setDisponibilidade(self, disponibilidade):
            self.disponibilidade = disponibilidade

        def getDisponibilidade(self):
            return self.disponibilidade

        def setDiasEmAtraso(self, diasEmAtraso):
            self.diasEmAtraso = diasEmAtraso

        def getDiasEmAtraso(self):
            return self.diasEmAtraso

        def setValor(self, valor):
            self.valor = valor

        def getValor(self):
            return self.valor

        def setTotal(self, total):
            self.total = total

        def getTotal(self):
            return self.total

        def setIdCliente(self, idCliente):
            self.idCliente = idCliente

        def getIdCliente(self):
            return self.idCliente

    def dump(self):
        return {"BookList": {'id': self.id,
                             'nome': self.nome,
                             'categoria': self.categoria,
                             'disponibilidade': self.disponibilidade,
                             'diasEmAtraso': self.diasEmAtraso,
                             'valor': self.valor,
                             'total': self.total,
                             'idCliente': self.idCliente}}
