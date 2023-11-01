from nodo import Nodo

class Pilha():
    def __init__(self):
        self.topo = None

    def adicionar(self,valor):
        nodo = Nodo(valor)
        topo = self.topo
        self.topo = nodo
        nodo.proximo = topo

    def remover(self):
        print("Removido: "+ str(self.topo))
        self.topo = self.topo.proximo

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