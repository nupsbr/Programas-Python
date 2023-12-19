'''mostre todos os numeros pares que estao no intervalo entre 1 a 50'''
print("NUMEROS PARES: ")
for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:  # se n for divisivel por 2 (n % 2)
        print(n, end=' ')
print("acabou!")
