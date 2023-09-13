tarifa = 1.99

class Conta:
    
    logado = True

    def __init__(self):
        self.__saldo = 0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Usuario não logado")
            return None

    def setSaldo(self,valor):
        if self.logado and valor >= 0.0:
            self.__saldo = valor
        else:
            print("Deve estar logado e o valor maior q 0")

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            print("Usuario não logado")
            return None

    @saldo.setter
    def saldo(self, valor):
        if self.logado and valor >= 0.0:
            self.__saldo = valor
        else:
            print("Deve estar logado")

    def __descontarTarifa(self):
        self.__saldo -= tarifa

    def depositar(self,valor):
        if self.__saldo + valor >= tarifa:
            self.saldo += valor
            self.__descontarTarifa()
        else:
            print("Valor insuficiente")

    def sacar(self,valor):
        if self.__saldo - valor >= tarifa:
            self.saldo -= valor
            self.__descontarTarifa()
        else:
            print("Valor insuficiente")