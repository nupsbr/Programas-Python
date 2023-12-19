'''leia o peso de 5 pessoas e mostre qual foi o maio e o menor peso lido'''

maior = 0
menor = 0
for i in range(1, 4):
    peso = float(input(f'Peso da {i} pessoa: '))

    if i == 1: # se é a primeira pessoa = coloca como maior e tb como menor peso
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(f'''\no maior peso {maior}
o menor peso {menor}''')
