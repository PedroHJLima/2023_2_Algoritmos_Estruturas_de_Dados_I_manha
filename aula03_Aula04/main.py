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

print("---------------Aula 4----------------")

from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido

beb = Categoria("Bebidas",1)
ali = Categoria("Alimentos",2)

prod01 = Produto("Coca-Cola",7.99,beb)
prod02 = Produto("Pepsi",5.99,beb)
prod03 = Produto("Trakinas",6.59,ali)

ped01 = Pedido("Rua A, 100",p2)
print(ped01)
ped01.addProduto(prod01)
print