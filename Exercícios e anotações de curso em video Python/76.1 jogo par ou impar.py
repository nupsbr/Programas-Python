from random import randint
vm = '\033[1;31m'
az = '\033[1;36m'
ptb = '\033[1;30;107m'
pt = '\033[1;30m'
lp = '\033[m'
print('=-' * 10)
print(f'{ptb}JOGO PAR OU ÍMPAR{lp}')
print('=-' * 10)
cont = 0
while True:
    sorteio = randint(1, 10)
    valor = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if jogador not in 'PIÍ':
        print('formato inválido')
        jogador = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if (sorteio + valor) % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'ÍMPAR'
    print(f'Você jogou {valor} e o computador jogou {sorteio}. Total de {sorteio + valor} deu {ptb}{parouimpar}{lp}')
    print('-' * 50)
    if jogador in 'IÍ' and parouimpar == 'ÍMPAR':
        print(f'{az}Você VENCEU!{lp}')
        print('-' * 50)
        print('Vamos jogar novamente...')
        cont += 1
    elif jogador in 'P' and parouimpar == 'PAR':
        print(f'{az}Voce VENCEU!{lp}')
        print('-' * 50)
        print(f'{pt}Vamos jogar novamente...{lp}')
        cont += 1
    else:
        break
if cont == 0:
    print(f'{vm}Game over{lp}. Você não venceu {pt}nenhuma vez{lp}, talvez na próxima... :( ')
elif cont == 1:
    print(f'{vm}Game over{lp}. Você venceu {az}1 vez{lp}! não é tudo aquilo, mas ainda é melhor que nenhuma :) ')
elif cont == 2 or 3:
    print(f'{vm}Game over{lp}. Você conseguiu vencer o computador {az}{cont} vezes{lp}, nada mal...')
else:
    print(f'{vm}Game Over{lp}. Você conseguiu vencer o computador {az}{cont} vezes{lp}! Surpreendente :)')