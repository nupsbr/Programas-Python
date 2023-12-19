# um professor quer sortear 1 de 4 alunos pra apagar o quadro. o programa deve receber o nome dos 4 alunos
# e escolher 1 aluno e escrever o nome do escolhido
import random

a1 = str(input('Digite o nome do 1 aluno: '))
a2 = str(input('Digite o nome do 2 aluno: '))
a3 = str(input('Digite o nome do 3 aluno: '))
a4 = str(input('Digite o nome do 4 aluno: '))

rint = random.randint(1, 4)

if rint == 1:
    print('Aluno:', a1)
elif rint == 2:
    print('Aluno:', a2)
elif rint == 3:
    print('Aluno:', a3)
elif rint == 4:
    print('Aluno:', a4)
