tupla = ('MESA', 'OLHO', 'TRABALHAR', 'CASA', 'BARRACA',
         'BARCO', 'FAROL', 'MARUJO', 'SEREIA')
for p in tupla:
    print(f'\n Na palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
