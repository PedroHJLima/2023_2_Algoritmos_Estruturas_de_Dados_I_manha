from veiculos import Veiculos

class Drone(Veiculos):
    def __init__(self, marca, modelo,helices:int):
        super().__init__(marca, modelo)
        self._helices = helices
        self.proximo = None

    def __str__(self):
        texto = super().imprimeVeiculo() + " Hélices: " + str(self._helices)
        return texto