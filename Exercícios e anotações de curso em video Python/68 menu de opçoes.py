'''leia dois valores e mostre um menu, seu programa devera realizar as op solcitadas em cada caso
1 - soma
2 - multiplicar
3 - maior 
4 - novos numeros
5 - sair'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

r = 0
while r != 5:
    print('''    
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR''')
    r = int(input("Qual é a sua opção: "))
    if r == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}')
    elif r == 2:
        print(f'A multiplicação de {n1} * {n2} = {n1*n2}')
    elif r == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif r == 4:
        print('Novos numeros')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5:
        print('saindo')
    else:
        print('TENTE NOVAMENTE')
