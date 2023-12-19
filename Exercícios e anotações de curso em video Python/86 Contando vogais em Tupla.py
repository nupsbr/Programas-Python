'''tenha uma tupla com varias palavras (nao usar acentos), depois, voce deve mostrar, para
cada palavra, quais sao as suas VOGAIS'''
tupla = ('MESA', 'OLHO', 'TRABALHAR', 'CASA', 'BARRACA',
         'BARCO', 'FAROL', 'MARUJO', 'SEREIA')
for com in tupla:
    print(f'Na palavra: {com} temos:', end=' ')
    a = com.count('A')
    e = com.count('E')
    i = com.count('I')
    o = com.count('O')
    u = com.count('U')
    print('A '*a, end='')
    print('E '*e, end='')
    print('I '*i, end='')
    print('O '*o, end='')
    print('U '*u, end='')
    print('\a')
