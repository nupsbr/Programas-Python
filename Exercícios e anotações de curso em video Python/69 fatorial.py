'''leia um numero qq e mostre seufatorial
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

w = int(input("Digite o numero para ver a seu fatorial: "))
c = w
f = 1
print(f'Calculando {w}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f'{f}')
