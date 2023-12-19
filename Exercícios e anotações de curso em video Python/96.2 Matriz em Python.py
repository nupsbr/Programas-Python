matriz = []
coluna_usuário = int(input('Quantas colunas a matriz terá: '))
linha_usuário = int(input('Quantas linhas a matriz terá: '))

for coluna in range(0, coluna_usuário):
    matriz.append([])
    for linha in range(0, linha_usuário):
        matriz[coluna].append(0)

print('-=' * 25)

for linha in range(0, linha_usuário):
    for coluna in range(0, coluna_usuário):
        matriz[linha][coluna] = int(
            input(f'Digite o valor para a [{linha}, {coluna}]: '))

for linha in range(0, linha_usuário):
    for coluna in range(0, coluna_usuário):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()