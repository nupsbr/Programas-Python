def fatorial(a, show=False):
    '''Calcula o fatorial de u numero
    :para a: o fatorial de um numero.
    :return: o valor do fatorial de um numero a'''
    c = a
    f = 1
    print(f'Calculando {a}!  = ', end='')
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        f = f * c
        c -= 1
    print(f'{f}')
    return f


fatorial(5)
help(fatorial)
