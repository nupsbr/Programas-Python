'''o pc vai pensar um numero de 0 a 10. so que agora o jogador vai tentar adivinhar ate acertar o numero
mostrando no final quantos palpites foram necessarios para vencer'''
import random
from time import sleep
import emoji


cores = {'pd': '\033[m',
         'vr': '\033[32m',
         'vlho': '\033[31m',
         'nrx': '\033[1;35m'}

co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[m'}


print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*10)
print(f"{cores['nrx']}A divinhe se o numero entre 0 a 10 !!!")
print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*10)

print(f"{cores['nrx']}PROCESSANDO...\n")
sleep(2)
al = random.randint(0, 10)
print("NUMERO GERADO!!\n")
sleep(1)
print(emoji.emojize("🤖Escolha um numero inteiro que acha que a maquina escolheu🎰🤖 "))
n = 0
b = 0
while al != n:
    n = int(input(emoji.emojize('Qual é o seu palpite🤔: ')))
    if n > al:
        print(emoji.emojize(
            f'{cores["vr"]}➖ Menos ➖{cores["nrx"]} ... tente mais uma vez'))
        b += 1
    elif n < al:
        print(emoji.emojize(
            f'{cores["vr"]}➕ Mais ➕{cores["nrx"]} ... tente mais uma vez'))
        b += 1

print(emoji.emojize(
    f'Acertou com {cores["vr"]}{b+1}{cores["nrx"]} tentativas. Parabens!🔥🔥🚀🔥🔥🚀🔥🔥🚀{cores["pd"]}'))
sleep(1)
print(emoji.emojize('🎆✨'))
sleep(1)
print(emoji.emojize('✨🎆✨'))
sleep(1)
print(emoji.emojize('🎆✨🎆✨🎆'))
sleep(1)
print(emoji.emojize('✨🎆✨🎆✨🎆✨'))
sleep(1)
print(emoji.emojize('🎆✨🎆✨🎆✨🎆✨🎆'))
sleep(1)
print(emoji.emojize('✨🎆✨🎆✨🎆✨🎆✨🎆✨🎆'))
