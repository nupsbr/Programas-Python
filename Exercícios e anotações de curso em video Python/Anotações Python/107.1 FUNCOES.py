# ---------------help()------------
def contador(i, f, p):
    '''faz uma contagem e mostra na tela
    ;pram i: inicio da contagem
    ;pram f: fim da contagem
    ;pram p: passo da contagem
    '''
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')


help(contador)  # vai mostrar oq a funcao contador faz
# funciona pra qualquer outra coisa help(print)

# ----------Parametros Opcionais---------


def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 6)
soma(1)
soma()


# --------Escopo de variavel-----

def funcao():
    n1 = 3  # variavel LOCAL
    print(f'N1 dentro vale {n1}')


n1 = 1  # variavel GLOBAL
funcao()
print(f'N1 fora vale {n1}')

# ----------RETURN-------------


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # retorna valor d s pra fora


resp = somar(3, 5, 7)  # valor de S vai pra resp


# -------------

def somarr(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somarr(3, 7, 3)
r2 = somarr(3, 3)
r3 = somarr(3)

print(f'Os resultado foram {r1} , {r2} e {r3}')

# ------ return par ou impar


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('é par')
else:
    print('nao é par')
