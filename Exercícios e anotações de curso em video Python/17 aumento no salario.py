# leia o salario e mostre seu novo salario com 15% de aumento

s = float(input('Digite seu salario:'))

print('Seu salario sem aumento é: {} e com 15%. de aumento vai ficar: {:.2f}'.format(s, s+s*15/100))
