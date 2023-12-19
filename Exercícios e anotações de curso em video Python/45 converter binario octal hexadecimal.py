'''Leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
1 - binario
2 - octal
3 - hexadecimal
'''

from time import sleep
co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[1;30;47m'}
print('{}{}◘{}◘{}◘{}◘{}{}'.format(
    co['pad'], co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*15)
print("\t BEM-VINDO AO CONVERSOR 3000")
print('{}{}◘{}◘{}◘{}◘{}{}'.format(
    co['pad'], co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*15)
sleep(2)
n = int(input("Adicione um numero inteiro para a conversao: "))
sleep(1)
print("\n{}1  {}BINARIO;{}".format(
    '\033[1;35;47m', '\033[1;34;47m', '\033[30;47m'))
sleep(1)
print("{}2  {}OCTAL;{}".format(
    '\033[1;35;47m', '\033[1;32;47m', '\033[30;47m'))
sleep(1)
print("{}3 {} HEXADECIMAL;{}".format(
    '\033[1;35;47m', '\033[1;31;47m', '\033[30;47m'))
sleep(1)

es = int(input("\nPara qual voce deseja converter: "))

# cores
cores = {'nor': '\033[1;30;47m', 'num': '\033[1;35;47m',
         'binario': '\033[1;34;47m', 'octal': '\033[1;32;47m', 'hexa': '\033[1;31;47m'}


if es == 1:
    print("\033[1;34;47m====== BINARIO ======\033[30;47m")
    print("{}{}{} para {}BINARIO: {}{}".format(
        cores['num'], n, cores['nor'], cores['binario'], bin(n), cores['nor']))

elif es == 2:
    print("{}====== OCTAL ======={}".format(cores['octal'], cores['nor']))
    print("{}{}{} para {}OCTAL: {}{}".format(
        cores['num'], n, cores['nor'], cores['octal'], oct(n), cores['nor']))

elif es == 3:
    print("{}==== HEXADECIMAL===={}".format(cores['hexa'], cores['nor']))
    print("{}{}{} para {}HEXADECIMAL: {}{}".format(
        cores['num'], n, cores['nor'], cores['hexa'], hex(n), cores['nor']))

else:
    print('''\t{}VOCE DIGITO ERRADO
        ESCOLHA UM DOS 3 NUMEROS!!{}'''.format(cores['hexa'], cores['nor']))
