'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte ao usuario qual sera
o valor a ser sacado (numero inteiro) e o programa vai informar quantas CEDULAS de cada valor serao entregue'''
print('===========================\n     BANCO   RICO \n===========================')
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced >0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break