from Desktop import Desktop
from NoteBook import NoteBook

compDesktops = []
compNotebooks = []

"""
---MODELO BASE PARA TESTES---
d1 = Desktop("modelo1","vermelho",10,220)
n1 = NoteBook("modelo2","azul",20,2)

d1.getInformacoes()
n1.getInformacoes()
"""

while True:
    print("\n"*2)
    escolha = int(input("1- Cadastra\n2- Imprime\nEscolha: "))

    if escolha == 1:
        tipo = int(input("\nQual o tipo?\n1-Desktop\n2-Notebook\nEscolha: "))
        if tipo == 1:
            #Quero cadastrar um desktop
            desktop = Desktop()
            desktop.cadastrar()
            compDesktops.append(desktop)
            dados = desktop.getInformacoes()
            modelo = dados[0]

            print(f"\nComputador {modelo} cadastrado!")

        if tipo == 2:
            #Quero cadastrar um notebook
            notebook = NoteBook()
            notebook.cadastrar()
            compNotebooks.append(notebook)
            dados = notebook.getInformacoes()
            modelo = dados[0]

            print(f"\nNotebook {modelo} criado!")

    if escolha == 2:
        #Imprimir a lista de todos criados
        if compDesktops:
            print("\n"*2 + "Lista de Computadores: ")
            for computadores in compDesktops:
                print(computadores)
        else:print("\nNenhum computador cadastrado")

        if compNotebooks:
            print("\n"*2 + "Lista de Notebooks: ")
            for notebooks in compNotebooks:
                print(notebooks)
        else:
            print("\nNenhum notebook cadastrado")

