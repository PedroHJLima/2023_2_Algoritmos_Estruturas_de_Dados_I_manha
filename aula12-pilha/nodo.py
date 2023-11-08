class Nodo:
    def __init__(self,nome,autor,n_pag):
        self.nome = nome
        self.autor = autor
        self.pag = n_pag
        proximo = None

    def __str__(self):
        return "Nome: " + self.nome+" Autor: "+self.autor+" Páginas: "+str(self.pag)