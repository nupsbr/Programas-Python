'''o jogo sera interrompido quando o jogador PERDE, mostrando o total de vitorias consecutivas que ele
conquistou no final do jogo'''
import random
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
pt = '\033[1;30m'
lp = '\033[m'
v = 0
print(f'{pt}-------------------\nJOGO {vr}IMPAR{pt} OU {az}PAR{pt}\n-------------------{lp}')
while True:
    valor = int(input('Diga um valor: '))
    pi = str(input(
        f'{az}Par{lp} ou {vr}Impar{lp}?  [{az}P{lp}/{vr}I{lp}]: ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(
            input(f'{pt}Dados invalidos. Por favor, informe {az}Par{pt} ou {vr}Impar{pt}?  [{az}P{lp}/{vr}I{pt}]:{lp}')).strip().upper()[0]
    pc = random.randint(1, valor)
    res = valor + pc
    if res % 2 == 0:  # deu par
        if pi in 'Pp':
            print(f'{vr}GANHOU!!{pt}\nVamos jogar novamnte...{lp}')
        elif pi in 'Ii':
            print(f'\n{vm}PERDEU !! :( {lp}\n Voce jogou {vr}{valor}{lp} e o computador {az}{pc}{lp}. total deu {vm}{res}{lp} = {az}PAR{lp}\n voce teve um total de {vr}{v}{lp} vitorias!')
            break
    else:
        if pi in 'Pp':
            print(f'\n{vm}PERDEU !! :( {lp}\n Voce jogou {vr}{valor}{lp} e o computador {az}{pc}{lp}. total deu {vm}{res}{lp} = {vr}IMPAR{lp}\n voce teve um total de {vr}{v}{lp} vitorias!')
            break
        elif pi in 'Ii':
            print(f'{vr}GANHOU!!{pt}\nVamos jogar novamnte...{lp}')
    v += 1
