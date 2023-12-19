from time import sleep

def separa():
    print('-='*20)


def contador(n1, n2, n3):
    if n1 < n2 or n3 < 0:
        separa()
        print(f'A contagem de {n1} ate {n2} de {n3} em {n3}:')
        for i in range(n1,n2+1,n3): 
            print(i, end=' ',flush=True) 
            sleep(0.1) 
        print('FIM')
    else:
        separa()
        print(f'A contagem de {n1} ate {n2} de {n3} em {n3}:')
        for i in range(n1,n2-1,-n3):   
            print(i, end=' ',flush=True)
            sleep(0.1)  
        print('FIM')
        separa()


contador(1, 10, 1)
contador(10, 1, 1)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))