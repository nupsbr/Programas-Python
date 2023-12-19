'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores PARES;
B) A soma dos valores da TERCEIRA COLUNA;
C) O MAIOR valor da segunda linha.(linha 1)'''
az = '\033[1;36m'
am = '\033[1;33m'
vr = '\033[1;32m'
vm = '\033[1;31m'
lp = '\033[m'
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = tcol = 0
for i in range(3):
    n = int(input(f'Digite um valor na linha {am}|{i}|{lp} : '))
    matriz[i][0] = n
    if n % 2 == 0:
        pares += n
    for j in range(2):
        n = int(input(f'Digite um valor na linha {am}|{i}|{lp} : '))
        matriz[i][j+1] = n
        if n % 2 == 0:
            pares += n
tcol = matriz[0][2] + matriz[1][2]+matriz[2][2]

print('-='*15)
print(f'{vr}{matriz[0]}\n{am}{matriz[1]}\n{az}{matriz[2]}{lp}')
print(f'A soma de todos os valores {vm}PARES{lp} é: {vm}{pares}{lp}')
print(f'A soma dos valores da {az}TERCEIRA COLUNA{lp} é: {az}{tcol}{lp}')
print(f'O {am}MAIOR{lp} valor da segunda linha: {am}{max(matriz[1])}{lp}')