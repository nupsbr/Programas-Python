'''Crie um programa que tenha uma tupla unica com nome de produtos e seus respectivos preços,
na sequencia. no final, mostre uma listagem de preços, organizando os dados em forma tabular'''

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('-'*30)
print('\tLISGEM DE PREÇOS')
print('-'*30)
pos = 0
for pos, comida in enumerate(produtos):
    if pos % 2 == 0:
        print('\a')
    else:
        for aa in range(0, 30):
            print(end='.')
        print('R$', end='')

    print(f'{comida:12}', end='')
    pos += 1
print('\n')
print('-'*30)
