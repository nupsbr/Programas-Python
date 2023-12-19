'''Leia i comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo e mostre
que tipo sera formado
EQUILATERO: Todos os lados iguais
ISOSCELES: Dois lados iguis
ESCALENO: Tdos os lados diferentes'''


print('=-'*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Os segmentos acima PODEM FORMAR um triangulo!")
    print('=-'*20)
    if r1 == r2 == r3:
        print("ESCALENO:")
    elif r1 == r2 or r3 == r1 or r2 == r3:
        print("ISOSCELES:")
    else:
        print("ESCALENO:")
else:
    print("Os segmentos acima NAO PODEM FORMAR um triangulo!")
    print('=-'*20)
