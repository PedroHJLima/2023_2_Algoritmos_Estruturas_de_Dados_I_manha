from abc import ABC,abstractmethod

class Computador():
    def __init__(self,modelo,cor,preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        return self.modelo,self.cor,self.preco
        
    def testaNum(numero):
        try:
            int(numero)
            return True
        except ValueError:
            return False
    
    @abstractmethod
    def cadastrar(self):
        modelo = input("Qual o nome do modelo?")
        cor = input("Qual a cor?")
        checando = True
        while checando:
            valor = input("Qual o preco?: ")
            if Computador.testaNum(valor):
                checando = False
            else:
                print("O preço não é um número válido.")

        return (modelo, cor, int(valor))