'''Leia 4 valores pelo teclado e guarde-os em uma tupla. no final mostre:
A) quant vezes apareceu o valor 9
B) em que posição foi citado o primeiro valor 3
C) quais foram os números pares'''
vr = '\033[1;32m'
lp = '\033[m'
vm = '\033[1;31m'
n = (int(input('Digite 1° numero: ')), int(input('Digite 2° numero: ')),
     int(input('Digite 3° numero: ')), int(input('Digite 4° numero: ')),)

print(f'Voce digitou os valores:{vr}{n}{lp}')
print(f'o valor {vm}9{lp} apareceu {vr}{(n.count(9))}{lp} vezes')
if 3 in n:
    print(f'o valor {vm}3{lp} apareceu na {vr}{(n.index(3))+1}°{lp} posicao')
else:
    print(f'{vm}O valor 3 nao foi digitado{lp}')
print(f'Os valores {vr}pares{lp} digitado foram:', end=' ')
for n in n:
    if n % 2 == 0:
        print(f'{vr}{n}{lp}', end=', ')
