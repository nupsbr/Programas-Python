from random import randint
maq = randint(1, 10)
ct = 0
while True:
    n = int(input('Digite um numero'))
    op = str(input('Digite par ou impar')).strip().upper()
    print('='*30)
    co = n+maq
    if co % 2 == 0 and op == 'P':
        print(f'Voce jogou {n} e o computador {maq}.total{co} deu PAR ')
        ct += 1
    if co % 2 != 0 and op == 'P':
        print(f'Voce jogou {n} e o computador {maq},total {co} Deu IMPAR')
        break
    if co % 2 == 0 and op == 'I':
        print(f'Voce jogou {n} e o computador {maq},total {co} DEU PAR')
        break
    if co % 2 != 0 and op == 'I':
        print(f'Voce digitou {n} e o computador {maq},total {co} Deu impar')
        ct += 1
print(f'Voce Venceu {ct} vez')
print('='*30)
