'''leia 5 val e guarde em uma lista, depois mostre qual foi o MAIOR e o MENOR valor digitado
e suas respectivas POSIÇÕES na lista'''
valor = list()
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print('-+'*30)
print(f'Voce digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} nas posições: ', end='')
for i, c in enumerate(valor):
    if c == max(valor):
        print(f'{i}...', end='')
print('\a')
print(f'O menor valor digitado foi {min(valor)} nas posições: ', end='')
for i, c in enumerate(valor):
    if c == min(valor):
        print(f'{i}...', end='')
