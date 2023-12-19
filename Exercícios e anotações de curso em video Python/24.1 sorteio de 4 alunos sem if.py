# um professor quer sortear 1 de 4 alunos pra apagar o quadro. o programa deve receber o nome dos 4 alunos
# e escolher 1 aluno e escrever o nome do escolhido
from random import choice

a1 = str(input('Digite o nome do 1 aluno: '))
a2 = str(input('Digite o nome do 2 aluno: '))
a3 = str(input('Digite o nome do 3 aluno: '))
a4 = str(input('Digite o nome do 4 aluno: '))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi:', escolhido)
