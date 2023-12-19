'''Função para finalizar while (fim) finaliza'''

def comhelp(str):
    while True:
        n = input(str).lower()
        if n != 'fim':
            print(help(n))
        else:
            print('FIM DO PROGRAMA')
            break


comhelp('Digite:  ')
