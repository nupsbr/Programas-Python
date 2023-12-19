print('='*50)  # imprime 30 vezes o =
n1 = float(input('Digite um valor: '))
n2 = float(input('Digire outro: '))
print('='*50)
s = n1 + n2  # soma
su = n1 - n2  # subitração
m = n1 * n2  # multiplicação
d = n1 / n2  # divisao
di = n1 // n2  # divisao inteira
e = n1 ** n2  # exponeciação

print('A soma é: {}, a subtração é: {}, a multiplicação é: {} e a divião é: {:.3f}'.format(s, su, m, d), end=(' '))#end= usa pra juntar os print
print('A divisão inteira é: {} e o exponeciação é: {}'.format(di, e))
