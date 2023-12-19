from time import sleep
from random import randint
lista = list()
vm = '\033[1;31m'
vr = '\033[1;32m'
az = '\033[1;36m'
lp = '\033[m'


def separa():
    print(f'{vm}-={lp}'*40)


def valores(lst, val):
    while val != 0:
        for i in range(val):
            lista.append(randint(0, 10))
        separa()
        print('Analisando os valores passados...')
        for j, v in enumerate(lista):  # com as posições
            print(f'{az}{v}{lp}', end=' ', flush=True)
            sleep(0.1)
        print(f'Foram informados {vr}{len(lista)}{lp} valores ao todo.')
        print(f'O maior valor informado foi {vr}{max(lista)}{lp}')
        val = len(lista) // 2
        lista.clear()
    separa()
    print(
        f'Foram informados {vr}0{lp} valores ao todo\n {az}Fim do programa!{lp}')


val = randint(0, 20)
valores(lista, val)
