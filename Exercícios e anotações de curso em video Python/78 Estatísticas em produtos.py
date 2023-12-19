'''leia o NOME e o PREÇO de varios produtos. o programa devera perguntar se o USUARIO vai continuar.
no final mostre:
A) qual é o total gasto na compra
B)quantos produtos custam mais de R$1000 (mil)
C)qual é o NOME do produto mais BARATO e seu preço'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
pt = '\033[1;30m'
lp = '\033[m'
tot = men = quant = menor = 0
print(f'{pt}------------------------\n{az}  LOJA {vr} SUPER {vm} BARATAO{pt}\n------------------------{lp}')
while True:
    prod = str(input('Nome do Produto: '))
    prec = float(input('Preço: R$'))
    cont = str(
        input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    tot += prec
    if prec > 1000:
        men += 1
    quant += 1
    if quant == 1 or prec < menor:
        menor = prec
        nom = prod
    if cont in 'S':
        continue
    elif cont in 'N':
        break
print(f'\nTotal da compra foi {vr}R${tot:.2f}{lp}')
print(f'Temos {vr}{men}{lp} produtos custando mais de {vr}R$1000.00{lp}')
print(f'O prduto mais barato foi {vr}{nom}{lp}  que custa {vr}R${menor:.2f}{lp}')
