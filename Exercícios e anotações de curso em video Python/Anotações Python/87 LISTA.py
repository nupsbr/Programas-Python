num = [1, 2, 3, 4]
num[2] = 3  # substitui valores na lista
num.append(7)  # add valor na lista
# inserir valor no meio da lista (na posição 2 add 0)
num.insert(2, 0)
print(num)
# ===ORDENAR===
num.sort()  # deixa em ordem
print(num)
num.sort(reverse=True)  # inverte a ordem
print(num)

print(f'essa lista tem {len(num)} elementos')

# ===REMOVER ITEM====
num.pop()  # remove o ultimo valor se nao tiver nada no ()
print(num)
num.pop(2)  # remove o elemento na posição 2
print(num)
num.remove(2)  # elemina o elemento 2 (so elemina o primeiro q ver)
print(num)
if 9 in num:  # se 9 esta na lista, remova numero 9
    num.remove(9)
else:
    print('Nao achei o numero 9')

# === MOSTRANDO USANDO FOR====
lista = []
lista.append(10)
lista.append(11)
lista.append(12)

for v in lista:
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(lista):  # com as posições
    print(f'na prosicao: {c} encontrei o valor {v}')
print('CHEGUEI AO FINAL DA LISTA!')
print('\n')


# ===ADD VALORES NA LISTA===

valor = list()
for cont in range(0, 3):
    valor.append(int(input('Digite um valor: ')))

for c, v in enumerate(valor):
    print(f'na prosicao: {c} encontrei o valor {v}')
print('CHEGUEI AO FINAL DA LISTA!')
print('\n')

# ===COPIAR UMA LISTA===

a = [1,2,3,4]
b = a[:] #b recebe todos os valores de a
print(f'Lista A:{a}')
b[2] = 8 #na posi 2 substitui por 8
print(f'Lista B:{b}')

