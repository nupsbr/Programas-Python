'''Crie um programa quetenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinta
seu programa devera ler um numero pelo teclado (entre 0 a 20) e a mostra-lo por extenso'''

numero = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
          'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {numero[n]}')
