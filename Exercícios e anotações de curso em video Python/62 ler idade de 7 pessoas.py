'''leia o ano de nascimento de 7 pessoas. no final mostre qnts pessoas ainda nao atingiram
e maioridade de quantos ja sao maiores '''
from datetime import date
m = 0
p = 0
for i in range(1, 8):
    n = int(input(f"Em que ano a {i} pessoa nasceu?  "))
    idade = date.today().year-n
    if idade <= 18:
        m += 1  #contador
    else:
        p += 1  #contador

print(f'''\nexiste {m} menores de idade
existe {p} MAIORES de idade''')
