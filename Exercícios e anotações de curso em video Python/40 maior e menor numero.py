'''ler tres numeros emostre qual e o menor e qual e o maior'''

n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero: "))
# verificar quem é o menor

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("o menor numero é {}".format(menor))
print("O maior numero é {}".format(maior))
