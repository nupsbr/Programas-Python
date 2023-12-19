from operator import itemgetter
pessoas = {'nome': 'Higor', 'sexo': 'M', 'idade': '23'}
print(pessoas)
print(pessoas['idade'])
# pra print formatado tem que usar ""
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())  # exibe os nomes das chaves
print(pessoas.values())  # exibe somente os valores
print(pessoas.items())  # exibe o dicionario todo

# -------------laços-----------
for k in pessoas.keys():  # chaves
    print(k)

for k in pessoas.values():  # valores
    print(k)

for k, v in pessoas.items():  # dicionario inteiro
    print(f'{k} = {v}')

# -------modificar dicionario--------
del pessoas['sexo']  # deleta sexo do dicionario
pessoas['nome'] = 'Julia'  # troca o valor de nome higor pra julia
# adicionar novo elemento no dicionario (nao precisa de dar append)
pessoas['peso'] = 46.5
print(pessoas.items())

# -------criar dicionario dentro de lista---------
brasil = []  # lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])  # exibe Rio de Janeiro

# ------------adicionar valores em um dicionario dentro de uma lista ----------
estado = dict()  # dicionario
brasil = list()  # lista
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # PRECISA USAR .copy() PARA ADICIONAR NA LISTA
    brasil.append(estado.copy())
for e in brasil:  # exibe a lista formatado
    for k, v in e.items():
        print(v, end=' ')
    print()

# -------------------------DEIXAR EM ORDEM----------------------
jogador = {'jogador 1': 4, 'jogador 2': 7,
           'jogador 3': 2, 'jogador 4': 8, 'jogador 5': 0, }
ranking = list()
# DEIXAR DICIONARIO EM ORDEM
# use(,reverse = True) caso for do maior ao menor
ranking = sorted(jogador.items(), key=itemgetter(1))
print('#'*50)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} tem {v[1]}')

# -------------------------DEIXAR EM ORDEM ATUALIZAÇÀO PYTHON 3.6+ (sem biblioteca)----------------------
jogador = {'jogador 1': 4, 'jogador 2': 7,
           'jogador 3': 2, 'jogador 4': 8, 'jogador 5': 0, }
c = 0
jogos2 = dict(sorted(jogador.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c += 1
