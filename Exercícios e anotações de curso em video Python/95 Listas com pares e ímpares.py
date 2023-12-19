'''crie um programa onde o usuario possa digitar 7 num e cadastre em uma lista unica que mantenha separado os valores
pares e impares. no final, mostre os valores pares e impare em ordem crescente'''

lista = []
lista_impar = []
lista_par= []

for i in range (0,7):
    lista.append(int(input(f'Digite o {i} valor: ')))
for c, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
        
lista.clear()
lista.append(lista_par[:])
lista.append(lista_impar[:])
lista[0].sort()
lista[1].sort()

print(lista)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')