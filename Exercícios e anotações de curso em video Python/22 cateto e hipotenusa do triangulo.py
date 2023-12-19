# leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa
import math

co = int(input('Digite o cateto Oposto: '))
ca = int(input('Digite o cateto Adjacente: '))

h = co ** 2 + ca ** 2

print('O comprimento da hipotenusa: {}'.format(math.sqrt(h)))
