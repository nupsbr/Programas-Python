from random import randint
lista = list()
vm = '\033[1;31m'
vr = '\033[1;32m'
az = '\033[1;36m'
lp = '\033[m'


def valores(lst):
    val = randint(0, 10)
    for i in range(val):
        lista.append(randint(0, 10))
    print(f'Sorteando {vr}{len(lista)}{lp} valores da lista: ', end='')
    for j, v in enumerate(lista):  # com as posições
        print(f'{az}{v}{lp}', end=' ', flush=True)
    print(f'{vr}PRONTO!{lp}')


def soma_par(lst):
    r = 0

    for c, i in enumerate(lista):
        if lista[c] % 2 == 0:
            r += lista[c]
            c = + c
        else:
            c = + c
    print(f'Somando os valores pares de {az}{lista}{lp}, temos {vr}{r}{lp}')


valores(lista)
soma_par(lista)
