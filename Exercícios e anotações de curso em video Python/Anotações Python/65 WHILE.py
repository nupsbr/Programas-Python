# contagem 1 a 10 com for
'''for c in range(1,10):
    print(c)
print('FIM')'''

# contagem de 1 a 10 com while
c = 1
while c < 10:
    print(c, end=' ')
    c = c + 1
print('FIM')

# loop com saida 0 para finalizar
c = 1
while c != 0:
    c = int(input('Digite um numer:'))
print('FIM')

# quer continuar?
r = 'S'
while r == 'S':
    n = int(input('Digite umvalor: '))
    r = str(input('Quer continuar [S/N]')).upper()
print('FIM')

# Numeros impares e pares  0 finaliza
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(F"VOCE DIGITOU {par} PARES E {impar} IMPARES")
