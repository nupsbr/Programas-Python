# leia o nome completo de uma pessoa e mostre o primeiro nome e o ultimo nome separadamente

nm = str(input('DIGITE SEU NOME COMPLETO: ')).split()

print('Primeiro nome: {}'.format(nm[0]))
print('Ultimo nome: {}'.format(nm[len(nm)-1]))
