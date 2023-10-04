from Pessoa import Pessoa
from AlunoGraduacao import AlunoGraduacao

listaAlunos = []

def listarAlunos():
    for aluno in listaAlunos:
        print(aluno)

#Criando novo aluno
aluno = AlunoGraduacao()
aluno.matricular()
listaAlunos.append(aluno)

#Listando todos os alunos matriculados
listarAlunos()

#Modificando a matricula de um aluno
aluno.alterarMatricula()

#Mostra que a matricula mudou
listarAlunos()

#+1 Presença do aluno
aluno.marcarPresenca()

