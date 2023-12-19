lista = []
maior = []
menor = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c}: ')))
print(f'Você digitou os valores {lista}')
for i, v in enumerate(lista):
    if v == max(lista):
        maior.append(i)
    if v == min(lista):
        menor.append(i)
print(f'O maior valor digitado foi {max(lista)} na posição {maior}')
print(f'O menor valor digitado foi {min(lista)} na posição {menor}')
