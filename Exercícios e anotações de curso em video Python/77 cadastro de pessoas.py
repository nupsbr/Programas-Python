'''leia a idade e sexo de varias pessoas. a cada pessoa cadastrada, o programa devera
perguntar se o usuario quer ou nao continuar. no final mostre;
A) qnts pessoas tem mais de 18 anos
B) qnts HOMENS foram cadastrados
C) qnts MULHERES tem menos de 20 anos.'''
m = p = d = 0
while True:
    print(
        '\033[1;31m-------------------\nCADASTRE UMA PESSOA\n-------------------\033[m')
    idade = int(input('Idade: '))
    sexo = str(
        input('Informe seu sexo: [\033[34mM\033[m/\033[31mF\033[m] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(
            input('Dados invalidos. Por favor, informe seu sexo [\033[34mM\033[m/\033[31mF\033[m]: ')).strip().upper()[0]
    cont = str(
        input('Quer continuar: [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input(
            'Dados invalidos. Por favor, informe quer continuar? [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().upper()[0]
    if idade < 20 and sexo == str('F'):
        p += 1
    if sexo == str('M'):
        m += 1
    if idade > 18:
        d += 1
    if cont in 'S':
        continue
    elif cont in 'N':
        break
print(
    f'\nTotal de pessoas com mais de \033[32m18\033[m anos: \033[32m{d}\033[m')
print(
    f'Ao todo são \033[32m{p}\033[31m mulheres\033[m com menos de \033[32m20\033[m anos')
print(f'E temos \033[32m{m}\033[34m homens\033[m cadastrados')
