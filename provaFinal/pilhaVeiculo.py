class PilhaVeiculo():
    def __init__(self):
        self.inicio = None

    def adicionarPilha(self,obj):
        if self.inicio == None:
            #Nenhum no inicio só adiciona
            self.inicio = obj
        else:
            #Tem um na fila pega ele primeiro
            aux = self.inicio
            self.inicio = obj
            self.inicio.proximo = aux

    def removerPilha(self):
        if self.inicio == None:
            print("Pilha Vazia")
        else:
            self.inicio = self.inicio.proximo

    def imprimePilha(self,obj):
        print("\n------Imprimindo Pilha de "+obj+"------")
        aux = self.inicio
        while aux:
            print(aux)
            aux = aux.proximo
