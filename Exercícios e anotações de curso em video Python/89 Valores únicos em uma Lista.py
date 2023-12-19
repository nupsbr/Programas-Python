'''crie um programa onde o usuario possa digitar varios valores e cadastre-os em uma lista.
caso o numero ja existe, ele NAO SERA ADICIONADO. No final serão exibidos todos os valores unicos digitados
em ordem crescente'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'
val = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in val:  # verifica se o numero ja tem na lista
        print(f'{vr}Dado registrado!{lp}')
        val.append(n)
    else:
        print(f'{vm}DADO JA CADASTRADO!!{lp}')
    cont = str(
        input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
val.sort()
print(f'Voce digitou os valores{az} {val}{lp}')
