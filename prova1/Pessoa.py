from abc import ABC,abstractmethod

class Pessoa():
    id = 1

    def __init__(self,id,nome,telefone):
        self.id = id
        self.nome = nome
        self._telefone = telefone

    @abstractmethod
    def marcarPresenca(self,presenca):
        presenca=+1
        return presenca

    def matricular(self):
        nome = input("Qual o nome do aluno?")
        telefone = input("Qual o telefone do aluno?")
        id =+ 1
        return id,nome,telefone