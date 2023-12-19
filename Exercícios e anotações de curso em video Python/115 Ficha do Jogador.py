
def ficha(nome, gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


nome=input('Nome:')
gols = input('Gols:')
ficha(nome = nome.strip() or "<desconhecido>",gols = gols.strip() or "0")
print(nome.strip())