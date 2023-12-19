num = [[], []] #lista com 2 listra dentro
val = 0
for i in range(1,8):
    val = int(input(f'Digite o {i} valor:'))
    if val %2 ==0:
        num[0].append(val)
    else:
        num[1].append(val)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')