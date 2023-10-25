class No:
    def __init__(self,valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return "Nó: " + str(self.dado) +str(self.proximo)+str(self.anterior)