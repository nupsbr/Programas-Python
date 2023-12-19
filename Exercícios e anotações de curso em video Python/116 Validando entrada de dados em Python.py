vm = '\033[1;31m'
lp = '\033[m'


def leiaint(msg):  # verifica se o n é um numero inteiro ou nao
    while True:
        n = (input(msg))
        if n.isnumeric():
            return n
        else:
            print(f'{vm}ERRO! Digite um numero inteiro valido.{lp}')


# Programa principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {vm}{n}{lp}')
