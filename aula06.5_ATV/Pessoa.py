class Pessoa():
    def __init__(self,codigo,nome,endereco,telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        return self.nome

    def _imprimeTelefone(self):
        print(self.__telefone)
