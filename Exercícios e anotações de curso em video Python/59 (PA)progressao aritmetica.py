'''Leia o primeiro terno e a razao de uma PA.
no final, mostre os 10 primeiros termos dessa progressao'''

print("="*35)
print("\t10 TERMOS DE UMA PA")
print("="*35)
t = int(input("Informe o primeiro termo: "))
r = int(input("razao: "))
d = t + (10 - 1)* r
for i in range(t, d, r):
    print(f'{i}', end=' -> ')
print('acabou')
