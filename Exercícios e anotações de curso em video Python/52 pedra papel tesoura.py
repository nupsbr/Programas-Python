'''Crie um programa que faça o computador joga JOKENPÔ com voce'''

from random import randint
itens = ("PEDRA", 'PAPEL', 'TESOURA')
computador = randint(0, 2)


jogador = int(input('''Escolha a opcao:
[0] = PEDRA
[1] = PAPEL
[2] = TESOURA

Qual é a sua Jogada?  '''))

print(f'''Computador jogou {itens[computador]}
Jogador jogou {itens[jogador]}''')

if computador == 0:  # computador PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif computador == 1:  # computador pepel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif computador == 2:  # computador tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")
