# leia um angulo qualquer e mostre o valor do SENO, COSSENO E TANGENTE
import math

angulo = int(input('Digite o angulo: '))
# Converter o ângulo para radianos
angulo_radianos = math.radians(angulo)

# Calcular o seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Imprimir os resultados
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
