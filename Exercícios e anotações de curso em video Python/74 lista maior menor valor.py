'''Leia varios num int. No final mostre a media entre todos os valores e qual foi o MAIOR  e o MENOR valor lidos
o programa deve perguntar ao usuario se ele quer ou nao CONTINUAR a digitar os valores'''
lista = []  # cria lista pra armazenar os num pra dps comparar quem é o maior e menor
soma = cont = n = 0  # junta tudo pq eles valem 0
n = int(input('Digite um numero: '))
while True:
    lista.append(n)  # Adiciona o número à lista
    soma += n
    cont += 1
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == str('S'):
        n = int(input('Digite um numero: '))
    elif continuar == str('N'):
        break
    else:
        print('DIGITE CERTO')
print(f'Voce digitou {cont} numeros e a media entre eles foi {soma/cont}')
print(f'O maior valor foi {max(lista)} e o menor foi {min(lista)}')
