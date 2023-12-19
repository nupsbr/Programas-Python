'''leia o ano de nascimento de 7 pessoas. no final mostre qnts pessoas ainda nao atingiram
e maioridade de quantos ja sao maiores '''
from datetime import date
atual = date.today().year
m = 0
p = 0
for n in range(1, 8):
    nasc = int(input(f"Em que ano a {n} pessoa nasceu?  "))
    idade = atual - nasc
    if idade >= 21:
        p += 1
    else:
        m += 1

print(f'''\nexiste {m} menores de idade
existe {p} MAIORES de idade''')
