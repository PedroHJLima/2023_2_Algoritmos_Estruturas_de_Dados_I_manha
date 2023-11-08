from nodo import Nodo

class Pilha():
    def __init__(self):
        self.topo = None

    def adicionar(self,valor,autor,pag):
        nodo = Nodo(valor,autor,pag)
        topo = self.topo
        self.topo = nodo
        nodo.proximo = topo

    def remover(self):
        if(self.topo != None):
            print("Removido: "+ str(self.topo))
            self.topo = self.topo.proximo
        else:
            print("Nenhum elemento para excluir!")

    def imprimir(self):
        print("-------")
        if self.topo == None:
            print("Pilha vazia")
        else:
            nodo = self.topo
            while nodo:
                print(nodo)
                nodo = nodo.proximo

        print("-------")

        #Adicionar nao precisa do if no caso do python.