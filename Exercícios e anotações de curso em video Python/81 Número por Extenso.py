'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinta
seu programa devera ler um numero pelo teclado (entre 0 a 20) e a mostra-lo por extenso'''
am = '\033[1;33m'
lp = '\033[m'
numero = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
          'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
n = int(input(f'Digite um numero entre {am}0{lp} a {am}20{lp}: '))
while n > 20 or n < 0:
    n = int(input(f'Dados invalidos. Por favor, numeros de {am}0{lp} a {am}20{lp}: '))
print(f'Voce digitou o numero {am}{numero[n]}{lp}')
