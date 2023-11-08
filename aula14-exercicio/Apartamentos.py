apartamentos =[]

class Apartamento():

    def __init__(self,id=None,numero=None,torre=None,vaga=None,proximo=None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self,id,numero,torre,vaga):
        apartamento = Apartamento(id,numero,torre,vaga)
        apartamentos.append(apartamento)

    def imprimir(self):
        if apartamentos != None:
            for i in range(len(apartamentos)):
                print(apartamentos[i])
        else: print("Nada")

    def __str__(self):
        return str(self.id)+str(self.numero)+str(self.torre)+str(self.vaga)+str(self.proximo)