'''leia um num inteiro e diga se ele é ou nao um numero primo'''
n = int(input("Digite um numero inteiro: "))
print('\033[0;33;44m OS NUMEROS DIVISIVEIS POR \033[4;32;45m{} \033[0;33;44m SÃO:\033[m'.format(n))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[4;32;45m', end='')
        total += 1
    else:
        print('\033[0;33;44m', end='')
    print('{}\033[m'.format(i), end='\033[1;33;44m|')
print('\nO numero {} foi dividido {} vezes!!'.format(n, total))
if total == 2:
    print("O numero é PRIMO\033[m")
else:
    print("Nao é primo\033[m")
