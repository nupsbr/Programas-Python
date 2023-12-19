import math
n = int(input('Digite um numero: '))
raiz = math.sqrt(n)  # raiz quadrada
print('A raiz de {} é igual a {}\n'.format(n, raiz))
print('A raiz de {} arredondado pra cima é igual a {}\n'.format( n, math.ceil(raiz)))  # arredonda pra cima
print('A raiz de {} arredondado pra baixo é igual a {}\n'.format( n, math.floor(raiz)))  # arredonda pra baixo
