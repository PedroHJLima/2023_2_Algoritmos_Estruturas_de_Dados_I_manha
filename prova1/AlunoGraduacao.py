from Pessoa import Pessoa

class AlunoGraduacao(Pessoa):
    contaMatricula = 1
    def __init__(self, id=0, nome="", telefone="",matricula="",presencas = 0):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.__presencas = presencas

    def matricular(self):
        dados = super().matricular()
        contaMatricula =+ 1

        self.id = dados[0]
        self.nome = dados[1]
        self._telefone = dados[2]
        self.__matricula = contaMatricula


    def __str__(self):
        frase = "Nome: "+str(self.nome)+"Telefone: "+str(self._telefone)+"Matricula: "+str(self.__matricula)
        return frase

    def marcarPresenca(self):
        self.__presencas = super().marcarPresenca(self.__presencas)
        print(self.__presencas)

    def mostraPresenca(self):
        return self.__presencas

    def alterarMatricula(self):
        matricula = input("Qual a nova matricula do aluno "+self.nome+"?")
        self.__matricula = matricula