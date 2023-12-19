'''mostrea a tabuada de um numero que o usuario escolher,
so que agora utilizando um laço for'''
n = int(input("Digite o numero para ver a sua tabuada: "))
for i in range(0, 11):
    print(f"{n} X {i} = {n*i}")
