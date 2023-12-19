# leia o preço do produto e mostre o prelo com 5% de desconto

p=float(input('Digite o preço do produto:'))

print('O produto sem desconto é: {} e com 5%, de desconto é: {}'.format(p,p-p*5/100))