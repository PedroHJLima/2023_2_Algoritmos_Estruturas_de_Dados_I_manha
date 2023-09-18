from Pessoa import Pessoa

class p_Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone,cpf,idade,peso,altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

        def imprimeCPF(self):
            return self.__cpf

        def __calcularIMC(self):
            return self.peso / (self.altura * self.altura)