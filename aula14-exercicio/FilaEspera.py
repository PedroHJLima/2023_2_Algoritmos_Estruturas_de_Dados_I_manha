from Apartamentos import Apartamento

class FilaEspera():
    def __init__(self):
        self.inicio = None

    def adicionar(self,apartamento):
        if self.inicio == None:
            self.inicio = apartamento
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = apartamento

    def imprimirFilaEspera(self):
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print("-------")
                print(aux)
                aux = aux.proximo