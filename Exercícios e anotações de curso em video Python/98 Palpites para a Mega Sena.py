'''faça um programa que ajude um jogador de mega sena a criar palpites, o programa deve perguntar quantos jogos
serao gerados e vai sortear 6 num entre 1 a 60 pra cada jogo, cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep
am = '\033[1;33m'
vr = '\033[1;32m'
lp = '\033[m'
conta = total = 0
lista = []
print(f'{am}•'*50, f'\n\t{vr}GERADOR DE NÚMEROS PARA MEGA SENA\n', f'{am}•{lp}'*50)
n = int(input('Quantos jogos voce que que eu sorteie?: '))
while total < n:
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            conta += 1
        if conta == 15:
            conta = 0
            break
    total += 1
    lista.sort()
    sleep(0.5)
    print(f'Jogo {vr}{total}{lp}: {am}{lista}{lp}')
    lista.clear()
print(f'{am}•'*50, f'\n\t\t{vr}BOA SORTE!\n', f'{am}•{lp}'*50)
