torres = []

class Torre():
    
    def __init__(self,id=0,nome=0,endereco=0):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self,id,nome,endereco):
        torre = Torre(id,nome,endereco)
        torres.append(torre)

        

    def imprimir(self):
        if torres != None:
            for i in range(len(torres)):
                print(torres[i])
        else: print("Nada")

    def __str__(self):
        return str(self.id)+self.nome+self.endereco