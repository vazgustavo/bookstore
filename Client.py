class Client:
    def __init__(self, id, nome, sobrenome, cpf, idLivro):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.idLivro = idLivro

        def setId(self, id):
            self.id = id

        def getId(self):
            return self.id

        def setNome(self, nome):
            self.nome = nome

        def getNome(self):
            return self.nome

        def setSobrenome(self, sobrenome):
            self.sobrenome = sobrenome

        def getSobrenome(self):
            return self.sobrenome

        def setCpf(self, cpf):
            self.cpf = cpf

        def getCpf(self):
            return self.cpf

        def setIdLivro(self, idLivro):
            self.idLivro = idLivro

        def getIdLivro(self):
            return self.idLivro

    def dump(self):
        return {"ClientList": {'id': self.id,
                               'nome': self.nome,
                               'sobrenome': self.sobrenome,
                               'cpf': self.cpf,
                               'idLivro': self.idLivro}}
