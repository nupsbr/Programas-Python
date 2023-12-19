def leiaInt(str):

    valor = input(str)
    while not valor.isnumeric(): #while not valor.isnumeric() é igual a while valor.isnumeric == False
        print('Erro. Introduza um número válido.')
        valor = input(str)
    return valor

#Programa Principal
n = leiaInt('Digite um número: ')
print(f'O número escrito foi {n}')