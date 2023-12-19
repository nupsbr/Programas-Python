# o prof quer sortear a ordem de apresentação de trabalho dos alunos,
# faça um programa que leia o nome dos quatro alunose mostre a ordem sorteada

from random import shuffle

a1 = str(input('Digite o nome do 1 aluno: '))
a2 = str(input('Digite o nome do 2 aluno: '))
a3 = str(input('Digite o nome do 3 aluno: '))
a4 = str(input('Digite o nome do 4 aluno: '))

lista = [a1, a2, a3, a4]

shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)
