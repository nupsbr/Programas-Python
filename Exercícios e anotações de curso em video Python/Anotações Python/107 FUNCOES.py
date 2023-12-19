def separa():
    print('-'*40)


def soma(a, b):
    print(f'A= {a} e B= {b} soma= {a+b}')


# programa principal
soma(4, 5)
soma(a=8, b=9)
soma(b=2, a=1)

separa()

# ----------for----------


def contador(*num):  # desmpacotar (pega varios numeros)
    print(num)  # criou uma tupla
    for valor in num:
        print(f'{valor} ', end='')
    print('fim')


contador(3, 4, 5, 6, 3, 2)
contador(4, 5, 7)

separa()

# ---------len--------


def contador_2(*num2):
    tam = len(num2)
    print(f'Recebi os valores {num2} e sao ao todo {tam} numeros')


contador_2(3, 4, 5, 6, 3, 2)
contador_2(4, 5, 7)

separa()

# --------lista e while--------


def dobra(lst):  # dobra valores na lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 7, 8, 5, 3, 5]
dobra(valores)
print(valores)

separa()
# -----desempacotar----


def soma_valores(*val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


soma_valores(4, 6)
soma_valores(5, 3, 5, 7, 5, 3)
