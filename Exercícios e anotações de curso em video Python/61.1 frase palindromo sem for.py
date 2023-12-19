'''leia uma frase qq e diga se ela é um PALINDROMO desconsiderando os espaços
EX: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

f = str(input("Digite uma frase: ")).strip().upper()
p = f.split()  # separa cada escrita
junto = ''.join(p)  # junta tudo sem espaços
print(f'frase: {junto}')
invertido = junto[::-1]
print("inverso: {}".format(invertido))

if junto == invertido:
    print('A frase é um PALINDROMO!!')
else:
    print('Nao é um palindromo!')
