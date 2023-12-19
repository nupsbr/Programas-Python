teste = list()  # 1 lista
teste.append('HIGOR')
teste.append(23)
galera = list()
galera.append(teste[:])  # galera recebe a 1 lista
print(galera)
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])  # usar [:] = copia o dados q esta na lista
print(galera)

# exibir uma parte da lista dentro de outra lista
pessoas = [['Joao', 12], ['ana', 22], ['carlos', 34]]
print(pessoas[2][1])  # mostra somente a idade de carlos

# mostrar dados das 2 listas usando for
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

# adicionar dados na lista dentro da outra

gente = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])  # copia dado pra gente
    dado.clear()  # deleta tudo em dado, deixando os dados somente em gente

print(gente)

# mostrar lista só com os maiores e menores de idade
totmai = totmen = 0
for p in gente:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade')
