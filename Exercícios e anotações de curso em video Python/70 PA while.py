'''Leia o primeiro terno e a razao de uma PA.
no final, mostre os 10 primeiros termos dessa progressao'''

print("="*35)
print("\t10 TERMOS DE UMA PA")
print("="*35)
t = int(input("Informe o primeiro termo: "))
r = int(input("razao: "))
d = t
contador = 1
while contador <= 10:
    print(f'{d}', end=' -> ')
    d += r
    contador += 1
print('acabou')
