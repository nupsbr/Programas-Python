'''ler varios num e colocar em uma lista. Depois disso, mostre:
A) Quantos numeros foram digitados
B) A lista de valores, ordenada de forma DRECESCENTE
C) Se o valor 5 foi digitado e esta ou nao na lista'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'
lista = []
while True:
    lista.append(int(input('Digite um numero:')))
    cont = str(input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break

lista.sort(reverse=True)
print(f'Voce digitou {az}{len(lista)}{lp} elementos!')  
print(f'Os valores em ordem decrescente são :{az}{lista}{lp}')
print(f"O numero {az}5 {vr}ESTA{lp} na lista!") if 5 in lista else print(f"O numero {az}5 {vm}NÃO ESTA{lp} na lista!")
