'''
        TUPLAS SAO IMUTAVEIS (n da pra mudar)
() <- Tupla
[] <- Lista
{} <- Dicionario


                0         1       2        3   '''
lanche = ('Hamburgues', 'Suco', 'Pizza','Pudim')#tb funciona sem o parenteses ()
print(lanche)  # todos
print(lanche[1])  # suco
print(lanche[-2])  # pizza
print(lanche[1:3])  # suco e pizza
print(lanche[2:])  # 2 ate o final
print(lanche[:2])  # do inicio ate o 2
print(len(lanche)) # mostra qnt itens tem dentro de lancha = 4

#pra tirar essa formatação: ('Hamburgues', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'vou comer: {comida}')
print('to cheio\n')

#outra maneira usando for
for cont in range(0, len(lanche)): #esse mostra a posicao da comida
    print(f'eu vou comer: {lanche[cont]}')#lanche na posicao cont
print('to cheio\n')

#outra maneira usando for tb pra mostrar a posicao
for pos, comida in enumerate(lanche):
    print(f'vou comer: {comida} na posicao {pos}')
print('to cheio\n')


print(sorted(lanche)) #deixa em ordem
print(lanche) 