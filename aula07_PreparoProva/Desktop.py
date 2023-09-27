from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo="", cor="", preco=1,fonte=110):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = fonte

    def getInformacoes(self):
        lista = super().getInformacoes()
        lista = lista + (self._potenciaDaFonte,)
        return (lista[0],lista[1],lista[2],lista[3])

    def cadastrar(self):
        dados = super().cadastrar()

        fonte = int(input("Qual a fonte do computador?"))
        
        self.modelo = dados[0]
        self.cor = dados[1]
        self.preco = dados[2]
        self._potenciaDaFonte = fonte

    def __str__(self):
        frase = "Modelo: "+str(self.modelo)+", Cor: "+str(self.cor)+", Preco: "+str(self.preco)+", Fonte: "+str(self._potenciaDaFonte)
        return frase