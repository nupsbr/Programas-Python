'''leia varios numeros e colocar em uma lista, depois disso crie listas extreas que vão conter apenas os valores
pares e os valores impares digitados, respectivamente. ao final, mostre o conteudo das tres listas geradas'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'

numeros = list()
par = list()
impar = list()

while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(
        input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
print(
    f'A lista completa é: {az}{numeros}{lp}\nA lista de {vr}PARES{lp} é: {vr}{par}{lp}\n A lista de {vm}IMPARES{lp} é: {vm}{impar}{lp}')
