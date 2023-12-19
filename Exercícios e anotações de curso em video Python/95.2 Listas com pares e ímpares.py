num = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c+1}º número: '))
    num[0].append(n) if n % 2 == 0 else num[1].append(n)
print('-' * 22, f'\nNúmeros pares: {sorted(num[0])}\nNúmeros ímpares: {sorted(num[1])}')