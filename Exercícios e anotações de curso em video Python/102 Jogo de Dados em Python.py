'''4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionario.
No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado'''
from random import randint
from operator import itemgetter
jogadores = {'jogador 1': 0, 'jogador 2': 0, 'jogador 3': 0, 'jogador 4': 0, }
ranking = list()
for k in jogadores.keys():  # chaves
    n = randint(1, 6)
    print(f'{k} tirou {n} no dado')
    jogadores[k] = n
#DEIXAR DICIONARIO EM ORDEM
ranking = sorted(jogadores.items(), key=itemgetter(1),reverse = True) 
print('+='*30,'\n\t\t===RANKING DOS JOGADORES===')
for i,v in enumerate(ranking):
    print(f'\t{i+1}° lugar: {v[0]} tirou {v[1]} no dado')

    