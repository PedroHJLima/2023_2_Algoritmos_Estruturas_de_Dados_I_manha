class Pessoa:
    def __init__(self,name,phone):
        self.nome = name
        self.fone = phone

    def __str__(self):
        text = "Nome: "+self.nome+"\n"
        text += "Telefone: "+self.fone
        return text 

    def imprimir(self):
        print(self)