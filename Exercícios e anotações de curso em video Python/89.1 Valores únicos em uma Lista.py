valor = []
while True:
    continuar = 'n/a'
    val = int(input('Digite um valor: '))
    if val in valor:
        print('Valor repetido, não será adicionado')
    else:
        valor.append(val)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).upper()
    if continuar in 'N':
        break
valor.sort()
print(f'Os Numeros adicionados foram em ordem crescente ', end='')
print(*valor, sep=', ')
