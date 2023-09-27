from Computador import Computador

class NoteBook(Computador):
    def __init__(self, modelo="", cor="", preco=1,bateria=110):
        super().__init__(modelo, cor, preco)
        self.__tempoBateria = bateria

    def getInformacoes(self):
        lista = super().getInformacoes()
        lista = lista + (self.__tempoBateria,)
        return(lista[0],lista[1],lista[2],lista[3])

    def cadastrar(self):
        dados = super().cadastrar()

        bateria = int(input("Quanto tempo de bateria em anos falta?: "))
        
        self.modelo = dados[0]
        self.cor = dados[1]
        self.preco = dados[2]
        self.__bateria = bateria

    def __str__(self):
        frase = "Modelo: "+str(self.modelo)+", Cor: "+str(self.cor)+", Preco: "+str(self.preco)+", Tempo de bateria: "+str(self.__bateria)
        return frase
    