'''leia n inteiro qq e mostre na tela os n primeirs elementos de uma sequencia fibonacci
EX: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

cont = int(input("Informe quantos numeros voce quer ver na sequencia fibonnaci: "))

n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end=' -> ')
contador = 3  # vai conta apartir do 3 pq ja mosta os 2 primeiros num n1 e n2 no printf
while contador <= cont:
    n3 = n1 + n2
    print(f'{n3}', end=' -> ')
    # vai passar pra frente, o 0 passa a valer 1 e o 1 passa a valer o resultado da soma (0+1) ou
    # seja n2 passa a valer 1, n3 vai ser a soma de n1 com n2 = 3
    n1 = n2
    n2 = n3
    contador += 1
print('FIM')
