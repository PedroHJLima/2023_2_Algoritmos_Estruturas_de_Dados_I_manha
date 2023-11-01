class Nodo:
    def __init__(self,valor):
        self.dado = valor
        proximo = None

    def __str__(self):
        return "Nó: " + str(self.dado)