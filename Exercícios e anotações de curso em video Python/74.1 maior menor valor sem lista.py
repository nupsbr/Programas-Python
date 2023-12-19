'''Leia varios num int. No final mostre a media entre todos os valores e qual foi o MAIOR  e o MENOR valor lidos
o programa deve perguntar ao usuario se ele quer ou nao CONTINUAR a digitar os valores'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    # vai deixar maiusculo tirar espaço e pegar somente o 1 caractere
    resp = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} numeros e a media entre eles foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
