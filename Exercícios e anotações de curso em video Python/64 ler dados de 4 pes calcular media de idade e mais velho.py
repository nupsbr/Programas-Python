'''Leia o nome, idade, sexo de 4 pessoa. no final do programa mostre
A media de idade do grupo
quantas mulheres tem
qual é o nome do homem mais velho
quantas mulheres tem menos de 20 anos'''
maior = 0
menor = 0
p = 0
media = 0
for i in range(1, 5):
    print(f'====={i} PESSOA ======')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo(M/F): ')).upper()
    # verifica se é homem e qual é o mais velho
    if sex == str('M'):
        if i == 1:
            maior = idade
            menor = idade
            nomemaior = nome
        else:
            if idade > maior:
                maior = idade
                nomemaior = nome
    # qnts mulheres é menor q 20 anos
    if idade < 20 and sex == str('F'):
        p += 1
    # media das idades
    media += idade

print(f'A media de idade do grupo é de {media/i} anos')
print(f'Ao todo são {p} mulheres com menos de 20 anos')
print(f'O homem mais velho tem {maior} anos e se chama {nomemaior}')
