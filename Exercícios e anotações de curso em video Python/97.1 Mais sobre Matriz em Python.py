matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = coluna3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
for linha in range(0, 3):
    coluna3 += matriz[linha][2]
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares digitados é: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print('Programa encerrado. Volte sempre! :)')