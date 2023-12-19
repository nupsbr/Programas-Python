# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas e minusculas
# quantas letras ao todo(sem considerar espaços)
# quantas letras tem o primeiro nome

fr = str(input('Digite seu nome completo: '))

print("seu nome em maiusculo é: {}".format(fr.upper()))
print("seu nome em minusculo é: {}".format(fr.lower()))
print("seu nome tem ao todos {} letras".format(len(fr)-fr.count(' ')))
print("seu primeiro nome tem {} letras".format(fr.find(' ')))
# outro modo
separa = fr.split()
print("seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))
