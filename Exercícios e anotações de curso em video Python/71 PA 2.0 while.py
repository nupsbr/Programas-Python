'''melhore o "PA while", perguntando para o usuario se ele que mostrar mais alguns termos.
o programa encerra enquando ele disse que quer mostrar 0 TERMOS'''
print("="*35)
print("\t10 TERMOS DE UMA PA")
print("="*35)
t = int(input("Informe o primeiro termo: "))
r = int(input("razao: "))
d = t
contador = 1
n = 10
contn = 0
while contador <= n:
    print(f'{d}', end=' -> ')
    d += r
    contador += 1
    contn += 1
print('PAUSA')
while True:
    n = int(input('Quantos termos voce quer mostrar mais?'))
    contador = 1
    if n == 0:
        break
    else:
        while contador <= n:
            print(f'{d}', end=' -> ')
            d += r
            contador += 1
            contn += 1
        print('PAUSA')
    contador = 1
print('PROGRMA FINALIZADO')
print(f'Progressao finalizada com {contn} termos mostrados')
