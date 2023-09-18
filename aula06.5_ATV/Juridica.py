from Pessoa import Pessoa

class p_Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone,CNPJ,inscricaoEstadual,quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__CNPJ = CNPJ
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.__CNPJ)

    def __emitirNotaFiscal():
        print("Nota fiscal")