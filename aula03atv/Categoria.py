
class Categoria():
    def __init__(self,nome = None,id = None):
        self.nome = nome
        self.id = id

    def __str__(self):
        return ("Categoria: " + self.nome + "id :" + str(self.id))

    def imprimir(self):
        print(str(self))
        