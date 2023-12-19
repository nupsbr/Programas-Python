'''leia o ano de nascimento de um jovem e informe de acordo com a sua idade, se ele AINDA VAI SE ALISTAR ao exercito,
se é a HORA DE SE ALISTAR ou se ja PASSOU DO TEMPO do alistamento
o programa tamebem devera mostrar o tempo que falta ou oque passou do prazo'''
from datetime import date
import emoji
co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[m'}
print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*20)
def anos(n):
    idade = date.today().year-n
    print('{}={}={}={}={}{}'.format(
        co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*20)
    if idade < 16:
       return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
        
n = int(input("Em que ano voce nasceu? "))
print(anos(n))