'''Faça u programa que leia nome e peso de varias listagem, guardando tudo em uma lista.
No final, mostre:
A) Qnts listagem foram cadastradas;
B) Uma listagem com as listagem mais pesadas;
C) Uma listagem com as listagem mais leves.'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'

temp = []
listagem = []

while True:
    no = str(input('Nome: '))
    pe = float(input('Peso: '))
    temp.append(pe), temp.append(no)
    listagem.append(temp[:])
    temp.clear()
    cont = str(
        input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
mai = max(listagem)[:][0]
min = min(listagem)[:][0]
print(f'Ao todo, tem {len(listagem)} listagem cadastradas!')
print(f'O {vr}MAIOR{lp} peso foi {az}{mai}Kg{lp}. Peso de ', end='')
for p in listagem:
    if p[0] == mai:
        print(f'{az}[{p[1]}] {lp}', end='')
print()
print(f'O {vm}MENOR{lp} peso foi {az}{min}Kg{lp}. Peso de ', end='')
for p in listagem:
    if p[0] == min:
        print(f'{az}[{p[1]}] {lp}', end='')
