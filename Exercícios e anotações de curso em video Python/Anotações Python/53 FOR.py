
for c in range(0, 6):
    print(f"oi {c}")
print("fim")

print('\n')

for c in range(0, 6, 2):  # pula de 2 em 2
    print(f"oi {c}")
print("fim")

print('\n')

for c in range(6, 0, -1):  # conta pra esquerda -
    print(f"oi {c}")
print("fim")

print('\n')

# colocando numero de repeticao dentro do for
n = int(input("Digite um numero: "))
for c in range(0, n+1):
    print(c)
print('fim')

print('\n')

# colocando inicio final e qnt de passos
i = int(input("inicio: "))
f = int(input("final: "))
p = int(input("passo: "))

for c in range(i, f+1, p):
    print(c)
print('fim')

# pergunta 3 vezes
for c in range(0, 3):
    n = int(input("Digite um valor:"))
print('fim')

print('\n')


# pergunta + soma
s = 0
for c in range(0, 3):
    n = int(input("Digite um valor:"))
    s += n
print(f'resultado:{s}')

print('\n')
