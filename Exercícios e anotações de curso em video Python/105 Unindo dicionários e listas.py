lista = list()
dados = dict()
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
rx = '\033[1;35m'
lp = '\033[m'
total_idade = 0
while True:
    dados['Nome'] = str(input(f'{rx}Nome: '))
    idade = int(input('Idade: '))
    dados['Idade'] = idade
    total_idade += idade
    sex = str(
        input(f'{rx}Sexo: [{vr}F{lp}/{vm}M{lp}{rx}]: ')).strip().upper()[0]
    while sex not in 'FM':
        sex = str(input(
            f'Por favor, digite apenas M ou F [{vr}F{lp}/{vm}M{lp}{rx}]: ')).strip().upper()[0]
    if sex in 'F' or 'M':
        dados['Sexo'] = sex
        lista.append(dados.copy())
        cont = str(
            input(f'{rx}Quer continuar? [{vr}S{lp}/{vm}N{lp}{rx}]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            f'Dados invalidos. Por favor, informe quer continuar? [{vr}S{lp}/{vm}N{lp}{rx}]: ')).strip().upper()[0]
    if cont in 'S':
        continue
    elif cont in 'N':
        break
    else:
        break

print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media_idade = total_idade / len(lista)
print(f'B) A média de idade é de {media_idade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=',')
for p in lista:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['Idade'] >= media_idade:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
