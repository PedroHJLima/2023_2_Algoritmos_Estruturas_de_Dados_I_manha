from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade("Viamão", 256302)

p1 = Pessoa("Pedro",1.70,c1)
#p2 = Pessoa("Maria",1.75,c1)
#p2 = Pessoa("Maria")
p2 = Pessoa("Maria", 1.7,city = c1)
p3 = Pessoa("José", 1.6 , c1)

print("IMC de ", p2.nome, "é: ", p2.getIMC(60))

p1.imprimir()