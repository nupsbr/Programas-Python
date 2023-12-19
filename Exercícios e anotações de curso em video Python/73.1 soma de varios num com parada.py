'''leia varios num int. o programa só vai parar quando o usuario digitar 999, que é a condição de parada.
No final, mostre quantos num foram digitados e qual a soma de todos eles (desconsiderando o 999)'''
soma = cont = n = 0  # junta tudo pq eles valem 0
n = int(input('Digite um numero [999 para parar!]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar!]: '))
# sem os - 1 e - 999
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
