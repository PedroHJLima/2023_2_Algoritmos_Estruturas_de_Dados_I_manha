"""numeros = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove")

while True:
    digitoInput = int(input("Digite um número de 0 a 9: "))

    def traduz(valor):
        print(numeros[valor])

    traduz(digitoInput)"""

boletim = {}

def calculaNota(n1,n2):
    notaFinal = (n1+n2/2)
    return notaFinal

nome = input("Qual o nome do aluno?")
n1 = int(input("Qual a nota do aluno?"))
n2 = int(input("Qual a outra nota do aluno?"))
notaFinal = calculaNota(n1,n2)

boletim["Nome"] = nome
boletim["Nota 1"] = n1
boletim["Nota 2"] = n2
boletim["Nota Final:"] = notaFinal

print(boletim)
