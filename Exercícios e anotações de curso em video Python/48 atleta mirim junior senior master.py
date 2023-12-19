'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade
9 anos : MIRIM
14 ANOS : INFANTIL
19 ANOS : JUNIOR
25 ANOS : SENIOR
ACIMA : MASTER'''

from datetime import date
n = int(input("Qual o seu ano: "))
idade = date.today().year-n
print("Quem nasceu em {} tem {} anos em {}".format(n, idade, date.today().year))

if idade <= 9:
    print("(A)O atleta tem {} e é MIRIM".format(idade))
elif idade <= 14:
    print("(A)O atleta tem {} e é INFANTIL".format(idade))
elif idade <= 19:
    print("(A)O atleta tem {} e é JUNIOR".format(idade))
elif idade <= 25:
    print("(A)O atleta tem {} e é SENIOR".format(idade))
else:
    print("(A)O atleta tem {} e é MASTER".format(idade))
