'''leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se por acaso
o CTPS for diferente de zero, o dicionario recebera tmbem o ano de contratação e o salario. Calcule e acrescente
além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
dici = {'Nome': str(input('Nome: ')), 'Idade': int(input(
    'Ano de Nascimento: ')), 'ctps': int(input('Carteira de trabalho(0 nao tem): '))}
dici['Idade'] = date.today().year-dici['Idade']
if dici['ctps'] != 0:
    dici['contratação'] = int(input('Ano de Contratação: '))
    dici['salário'] = float(input('Salário: R$'))
    dici['aposentadoria'] = dici['Idade'] + \
        (dici['contratação']+35)-date.today().year
    print('=-'*25)
    for k, v in dici.items():
        print(f'\t - {k} tem o valor {v}')
else:
    print('=-'*25)
    for k, v in dici.items():
        print(f'\t - {k} tem o valor {v}')
