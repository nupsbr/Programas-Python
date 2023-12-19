'''Digite 5 num e cadastre em uma lista, ja no posição correta de inserção (sem usar o sort).No final,
mostre a lista ordenada na tela'''
lista = []
for i in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:  # verifica em cada posição é menor ou igual a n
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista')
                break
            pos += 1
print(f'\n Os valores digitados em ordem foram {lista}')
