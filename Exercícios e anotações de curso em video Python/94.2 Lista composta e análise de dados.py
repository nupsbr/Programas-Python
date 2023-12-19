
pessoas = list()
dados = list()  # Lista temporária
maior_peso = menor_peso = float(0)

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if maior_peso < dados[1]:
            maior_peso = dados[1]
        if menor_peso > dados[1]:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('Comando Inválido!')
        else:
            break
    if continuar == 'N':
        break

print('-'*49)
print(f'N° de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso foi de {maior_peso}Kg. Peso de ', end='')
for c, pessoa in enumerate(pessoas):
    if pessoas[c][1] == maior_peso:
        print('[', end='')
        print(pessoas[c][0], end='] ')
print(f'\nMenor peso foi de {menor_peso}Kg. Peso de ', end='')
for c, pessoa in enumerate(pessoas):
    if pessoas[c][1] == menor_peso:
        print('[', end='')
        print(pessoas[c][0], end='] ')
