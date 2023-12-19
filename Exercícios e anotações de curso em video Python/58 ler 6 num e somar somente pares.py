'''Leia 6 numeros int e mostre a soma apenas dos PARES e se for impar, desconsidere-o'''
soma = 0
for i in range(1, 7):
    n = int(input(f"Digite o {i} numero inteiro: "))
    if n % 2 == 0:
        soma = soma + n
print(f"A soma de todos os pares é de: {soma}")
