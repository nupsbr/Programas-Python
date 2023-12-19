from time import sleep
def contador(a, b, c):
    if c == 0:
        c += 1
        print('O número digitado não é válido. Será realizada a contagem com o PASSO = 1')
    if a > b and c > 0 or b > a and c < 0:
        c *= -1
    for d in range(a, b+1, c):
        print(f'{d}', end=' ')
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('De: ')), int(input('Até: ')), int(input('Passo: ')))