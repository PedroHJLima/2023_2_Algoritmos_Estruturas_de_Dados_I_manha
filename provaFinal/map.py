def adicionarValores(listaValores):
    resultado = 0
    for valor in listaValores:
        resultado = resultado + valor 
    return resultado

lista1 = 2,4
lista2 = 4,5,6,7,8
lista3 = 1,3,3
print (lista1)

resultados = map(adicionarValores, (lista1,lista2,lista3))
print(list(resultados))