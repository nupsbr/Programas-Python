'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte ao usuario qual sera
o valor a ser sacado (numero inteiro) e o programa vai informar quantas CEDULAS de cada valor serao entregue'''
vm = '\033[1;31m'
az = '\033[1;36m'
vr = '\033[1;32m'
am = '\033[1;33m'
rx = '\033[1;35m'
ptb = '\033[1;30;107m'
pt = '\033[1;30m'
lp = '\033[m'
print(f'{am}===========================\n     BANCO  HIGOR       \n==========================={lp}')
t200 = t100 = t50 = t20 = t10 = t5 = t1 = 0
val = int(input(f'{pt}Que valor você quer sacar? {vr}R$'))
while val >= 200:
    val -= 200
    t200 += 1
while val >= 100:
    val -= 100
    t100 += 1
while val >= 50:
    val -= 50
    t50 += 1
while val >= 20:
    val -= 20
    t20 += 1
while val >= 10:
    val -= 10
    t5 += 1
while val >= 5:
    val -= 5
    t5 += 1
while val >= 1:
    val -= 1
    t1 += 1
if t200 > 0:
    print(f'{pt}Total de {vr}{t200}{pt} celulas de {vr}R$200{lp}')
if t100 > 0:
    print(f'{pt}Total de {vr}{t100}{pt} celulas de {vr}R$100{lp}')
if t50 > 0:
    print(f'{pt}Total de {vr}{t50}{pt} celulas de {vr}R$50{lp}')
if t20 > 0:
    print(f'{pt}Total de {vr}{t20}{pt} celulas de {vr}R$20{lp}')
if t10 > 0:
    print(f'{pt}Total de {vr}{t10}{pt} celulas de {vr}R$10{lp}')
if t5 > 0:
    print(f'{pt}Total de {vr}{t5}{pt} celulas de {vr}R$5{lp}')
if t1 > 0:
    print(f'{pt}Total de {vr}{t1}{pt} celulas de {vr}R$1{lp}')
