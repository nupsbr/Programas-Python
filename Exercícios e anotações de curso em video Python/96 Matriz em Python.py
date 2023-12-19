'''Crie um programa que  crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
no final, mostre a matriz na tela com a formatação correta'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    n = int(input(f'Digite um valor na linha |{i}| : '))
    matriz[i][0] = n
    for j in range(2):
        n = int(input(f'Digite um valor na linha |{i}| : '))
        matriz[i][j+1] = n
print('-='*15)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
