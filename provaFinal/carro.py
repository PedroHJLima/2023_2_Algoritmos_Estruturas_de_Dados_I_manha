from veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, marca, modelo,portas:int):
        super().__init__(marca, modelo)
        self.__portas = portas
        self.proximo = None

    def __str__(self):
        texto = super().imprimeVeiculo() + " Portas: "+ str(self.__portas)
        return texto