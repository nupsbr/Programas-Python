'''Gere 5 num aleatorios e colocar em uma tupla. depois disso, motre a listagem de numeros gerado
e tambem indique o menor e o maior valor que estao na tupla'''
rx = '\033[1;35m'
vm = '\033[1;31m'
az = '\033[1;36m'
lp = '\033[m'
from random import randint
numeros = tuple(randint(1, 10) for i in range(5)) #for dentro da tupla
print(f'Os valores sorteados foram:{rx}{numeros}{lp}')
print(f'O {vm}MENOR{lp} valor é:{vm}{min(numeros)}{lp}')
print(f'O {az}MAIOR{lp} valor é:{az}{max(numeros)}{lp}')
