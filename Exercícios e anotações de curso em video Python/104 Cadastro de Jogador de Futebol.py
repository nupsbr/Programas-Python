dici = {'Nome': str(input('Nome do jogador: ')), 'Total': 0}
lista = []
partidas = int(input(f'Quantas partidas {dici["Nome"]} jogou? '))
for i in range(partidas):
    lista.append(int(input(f'Quantos gols na partida {i+1}? ')))
    dici["Gols"] = lista[:]  # copia a lista
i = 0
for c, v in enumerate(lista):  # com as posições
    i += v
dici["Total"] = i
print('=-'*40)
print(dici)
print('=-'*40)
for k, v in dici.items():  # dicionario inteiro
    print(f'O campo {k} tem o valor {v}')
print('=-'*40)
print(f'O jogador {dici["Nome"]} jogou {partidas} partidas.')
for k, v in enumerate(lista):
    print(f'=> Na {k+1}° parida, fez {v} gols.')
print(f'Foi um total de {i} gols.')
