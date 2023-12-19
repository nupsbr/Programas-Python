'''Mostre a tabuada de arios num, um de cada v ez, para cada valor digitado pelo usuario.
o programa sera interrompido qnd o num solicitado for negativo'''
while True:
    n = int(input('Digite um numero:'))
    if n >= 0:
        for i in range(1, 11):
            print('{}x{}={}'.format(n, i, n*i))
    else:
        break
print('Acabou')
