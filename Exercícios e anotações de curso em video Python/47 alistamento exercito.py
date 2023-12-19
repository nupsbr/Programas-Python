'''leia o ano de nascimento de um jovem e informe de acordo com a sua idade, se ele AINDA VAI SE ALISTAR ao exercito,
se é a HORA DE SE ALISTAR ou se ja PASSOU DO TEMPO do alistamento
o programa tamebem devera mostrar o tempo que falta ou oque passou do prazo'''
from datetime import date
import emoji
co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[m'}
print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*20)
n = int(input("Qual o seu ano: "))
idade = date.today().year-n
print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*20)
if idade < 18:
    print("Ainda falta {} anos para o alistamento".format(18 - idade))
    print("Seu alistamento sera em {}".format(
        date.today().year + (18 - idade)))
elif idade > 18:
    print("Voce é bom em se esconder, e foi alistado ha {} anos.".format(idade - 18))
    print("Seu alistamento foi em {}".format((18 - idade) + date.today().year))
else:
    print(emoji.emojize(
        "\t\033[4;33m⚠️ ⚠️ ⚠️ ⚠️  CUIDADO!! SE ESCONDA IMEDIATAMENTE !! ⚠️ ⚠️ ⚠️ ⚠️\033[m"))
