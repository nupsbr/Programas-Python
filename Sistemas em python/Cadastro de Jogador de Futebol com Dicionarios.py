from time import sleep

vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'

lista_jogadores = []  # lista

while True:
    jogador = {}  # dicionario
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input('Quantas partidas jogou: '))

    jogador['gols'] = []  # lista dentro do dicionario

    for i in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    lista_jogadores.append(jogador.copy())
    cont = str(
        input(f'Quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
while True:
    print('-=' * 40)
    print('cod Nome\tPartidas\tGols\t\tTotal')
    print('-' * 70)
    for i, jogador in enumerate(lista_jogadores):
        print(i, end=' ')
        for k, v in jogador.items():
            print(f'{v}', end='\t\t')
        print()
    print('-' * 70)
    op = int (input('Mostrar dados de qual jogador? (999 para parar)'))
    if op == 999:
       break
    if op >= len(lista_jogadores):
        print('-' * 70)
        print("Código de jogador não existe. Por favor, tente novamente.")
    else:
        print('-' * 70)
        print(f'O jogador {lista_jogadores[op]["nome"]} tem {lista_jogadores[op]["partidas"]} partidas.')
        for c in range(0, lista_jogadores[op]["partidas"]):
            print(f'   => Na partida {c+1} fez {lista_jogadores[op]["gols"][c]} gols.')
        print(f'E fez um total de {lista_jogadores[op]["total"]} gols.')
        sleep(2)