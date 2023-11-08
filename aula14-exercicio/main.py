from Torre import Torre,torres
from Apartamentos import Apartamento,apartamentos
from FilaEspera import FilaEspera



torre = Torre()
apartamento = Apartamento()
filaEspera = FilaEspera()

torre.cadastrar(1,"Torre1","AvenidaBrasil")
torre.cadastrar(2,"Torre 2", "Avenida Brasilia")
#torre.imprimir()
apartamento.cadastrar(1,205,torres[1],2)
apartamento.cadastrar(2,305,None,2)
#apartamento.imprimir()

filaEspera.adicionar(apartamentos[0])
filaEspera.imprimirFilaEspera()
filaEspera.adicionar(apartamentos[1])
filaEspera.imprimirFilaEspera()