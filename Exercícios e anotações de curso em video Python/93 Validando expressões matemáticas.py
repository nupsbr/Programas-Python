'''digite uma expressão qualquer que use PARENTESES. Seu aplicativo devera analisar se a expressão passada
esta com os parenteses abertos e fechados na ordem correta'''

n = input('Digite sua expressão: ')
j = n.count('(')
d = n.count(')')
a = j+d
print(j+d)
if a % 2 == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')
