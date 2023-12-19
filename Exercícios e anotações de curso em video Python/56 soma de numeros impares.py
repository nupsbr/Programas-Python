'''Calcule a soma entre todos os numeros impares que sao multiplos de tres e q se encontram no intervalo
de 1 ate 500'''
soma= 0
cont = 0
for a in range(1, 501, 2):
    if a %3 ==0: #sao divisiveis por 3
        cont = cont + 1
        soma = soma +a
print(f"a soma de todos os {cont} valores é {soma}")