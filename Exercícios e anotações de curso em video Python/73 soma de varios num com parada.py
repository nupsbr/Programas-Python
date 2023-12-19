'''leia varios num int. o programa só vai parar quando o usuario digitar 999, que é a condição de parada.
No final, mostre quantos num foram digitados e qual a soma de todos eles (desconsiderando o 999)'''
soma = cont = n = 0  # junta tudo pq eles valem 0
while n != 999:
    n = int(input('Digite um numero [999 para parar!]: '))
    soma += n
    cont += 1
print(f'Voce digitou {cont - 1} numeros e a soma entre eles foi {soma - 999}')
