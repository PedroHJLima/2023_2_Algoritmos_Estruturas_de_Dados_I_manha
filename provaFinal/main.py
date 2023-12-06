from carro import Carro
from drone import Drone
from pilhaVeiculo import *

pilhaCarro = PilhaVeiculo()
pilhaDrone = PilhaVeiculo()

def criarVeiculo(tipo):
    marca = input("Qual a marca do "+tipo+"? ")
    modelo = input("Qual o modelo do "+tipo+"? ")
    if tipo == "Carro":
        portas = input("Quantas portas tem?")
        return marca,modelo,portas
    elif tipo == "Drone":
        helices = input("Quantas helices tem? ")
        return marca,modelo,helices
    
while True:
    escolha = input("\nQual pilha deseja utilizar?\n1- Carros\n2- Drones\n3- Imprimir Pilhas\n")
    if escolha == "1":
        #Mexer na lista de carros
        opcao = input("O que deseja fazer?\n1- Adicionar Carro\n2- Remover Carro\n")
        if opcao == "1":
            informacoes = criarVeiculo("Carro")
            carro = Carro(informacoes[0],informacoes[1],informacoes[2])
            try:
                pilhaCarro.adicionarPilha(carro)
            except:
                print("Informações erradas")

        elif opcao =="2":
            pilhaCarro.removerPilha()
            print("Carro Removido!")
        
        else:
            print("Voltando ao menu")

    elif escolha == "2":
        #Mexer na lista de Drones
        opcao = input("O que deseja fazer?\n1- Adicionar Drone\n2- Remover Drone\n")
        if opcao == "1":
            informacoes = criarVeiculo("Drone")
            drone = Drone(informacoes[0],informacoes[1],informacoes[2])
            pilhaDrone.adicionarPilha(drone)

        elif opcao =="2":
            pilhaDrone.removerPilha()
            print("Drone Removido!")
        
        else:
            print("Voltando ao menu")

    elif escolha == "3":
        pilhaCarro.imprimePilha("carro")
        pilhaDrone.imprimePilha("drone")