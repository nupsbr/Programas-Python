'''leia um numero qq e mostre seufatorial
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
w = int(input("Digite o numero para ver a seu fatorial: "))
f = factorial(w)
print(f'O fatorial de {w} é {f}')