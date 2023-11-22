carros = "Uno","Doblo","Toro","Jeep"
print(carros[1])

print(carros[0:-3])

itens =carros[3:],carros[0]
print(itens)

def calcular(x,y):
    return x+y,x-y,x*y,x/y

resultado = calcular(10,2)
print("Result: ",resultado)
print("Soma: ",resultado[0])

a, b,_,_= calcular(9,3)
print("A: ",a)
print("B: ",b)