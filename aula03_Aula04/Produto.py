from Categoria import Categoria

class Produto():
    def __init__(self,nome,preco,categoria = Categoria()):
        self.nome = nome
        self.preco = preco
        self.cat = categoria

    def __str__(self) -> str:
        #No caso do método imprimir, ele não retorna dado nenhum, então usá-lo no return quebra o código
        #return ("Nome: "+self.nome+"\nPreco: "+str(self.preco)+"\nCategoria: "+ self.cat.imprimir())
        #Usar esse
        return ("Nome: "+self.nome+"\nPreco: "+str(self.preco)+"\nCategoria: "+ str(self.cat))
        

    def imprimir(self):
        print(str(self))