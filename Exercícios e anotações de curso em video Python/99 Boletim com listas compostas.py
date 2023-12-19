'''leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. no final, mostre um boletim 
contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente'''
from time import sleep
boletim = list()
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
rx = '\033[1;35m'
lp = '\033[m'
while True:
    nome = str(input(f'{az}Nome do aluno: {rx}'))
    n1 = float(input(f'{az}Nota 1: {rx}'))
    n2 = float(input(f'{az}Nota 2: {rx}'))
    media = (n1 + n2)/2
    boletim.append([nome, n1, n2, media])  # usar [[]] cria uma lista composta
    cont = str(
        input(f'{rx}Quer continuar? [{vr}S{lp}/{vm}N{lp}{rx}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}{rx}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
print(f'{rx}Nº\t|\tNOME\t|\tMEDIA\t|')
for c, n in enumerate(boletim):
    print(f'{az}{c}\t|\t{n[0]}\t|\t{n[3]}\t|')
    sleep(0.5)
sleep(2)
while True:
    cont = str(
        input(f'{lp}Quer a ver Nota de Algum aluno em especifico? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        while True:
            print(f'{lp}Para sair Digite {vm}(999){lp}')
            num = int(input(f'Informe o {rx}Nº{lp} do Aluno que deseja ver: '))
            if num == 999:
                break
            print(f'{rx}NOME\t|\tNOTA 1\t|\tNOTA 2\t|\tMEDIA\t|')
            print(f'{az}{boletim[num][0]}\t|\t{boletim[num][1]}\t|\t{boletim[num][2]}\t|\t{boletim[num][3]}\t|\n')
            sleep(3) 
    elif cont in 'N':
        break
print(f'\n\t\t{vr}VOLTE SEMPRE!{lp}')