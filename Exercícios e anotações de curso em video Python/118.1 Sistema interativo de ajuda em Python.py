'''VERSÃO 2 = Função para finalizar while (fim) finaliza'''

def comhelp(str):
    while True:
        n = input(str).lower()
        if n == 'fim':
            break
        else:
            print(help(n))


comhelp('Digite:  ')
