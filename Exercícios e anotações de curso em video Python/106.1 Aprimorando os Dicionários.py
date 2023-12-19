fut=dict()
gol=list()
elenco= list()
while True:

    fut['name']= str(input('player name: '))
    p= int(input(f'quantas partidas {fut["name"]} jogou? -'))
    for c in range(0,p):
        gol.append(int(input(f'quantos gols na patida {c+1} ?')))
    print('-='*20)
    fut['gols'] = gol[:]
    fut['total']= sum(gol)
    elenco.append(fut.copy())
    v=' '
    while v not in 'sn':
        v = str(input('Deseja Continuar? [S/N]')).lower().strip()[0]
        if v not in'sn':
            print('didite apenas [s] ou [n]')
    if v == 'n':
        break

print('-='*20)
print(f'cod  name          gols        total')
print('--'*15)
for i,v in enumerate(elenco):
    print(f'{i} {v["name"]:<}        {v["gols"]}     {v["total"]:>4}')
ind  = 0
print('--'*15)
cont=0
while True:
    ind= int(input('digite o cod do jogador para ver seus resultados ou (999 para sair)'))
    if ind != len(elenco):
        if ind == 999:
            print(f' ATÉ A PROXIMA !!!')
        else:
            while ind >= len(elenco) :
                print(f'Digite um Codigo Valido!!!')
                ind = int(input('digite o cod do jogador para ver seus resultados ou (999 para sair)'))

    if ind in range(0,len(elenco)):
        print('--' * 15)
        print(f'LEVANTAMENTO DO JOGADOR {elenco[ind]["name"]}:')
        for c in range(1,len(fut["gols"])+1):
            print(f'no jogo {c} converteu {elenco[ind]["gols"][c-1]}')
            print('--' * 15)

    if ind == 999:
        break