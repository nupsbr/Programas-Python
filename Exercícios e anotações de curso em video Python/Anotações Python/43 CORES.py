'''
STILO DE FONTE:         COR TEXTO:        COR FUNDO:
0 PADRAO                30 BRANCO        40 BRANCO
1 NEGRITO               31 VERMELHO      41 VERMELHO
4 SUBLINHADO            32 VERDE         42 VERDE
7 NEGATIVO              33 AMARELO       43 AMARELO
                        34 AZUL          44 AZUL
                        35 ROXO          45 ROXO
                        36 AQUA          46 AQUA
                        37 CINZA         47 CINZA

EXEMPLO:     \033[0;33;44m  <-- A COR VAI ATE O FINAL

             \033[0;33;44m TEXTO \033[m <-- A COR SE APLICA SOMENTE NO PRINT
'''
print("\033[30;47m BRANCO E CINZA \033[m\n")

print("\033[1;31;46m NEGRITO VERMELHO AQUA \033[m\n")

print("\033[4;32;45m SUB VERDE ROXO\033[m\n")

print("\033[0;33;44m SEM NEGATIVO AMARELO AZUL\033[m\n")

print("\033[7;33;44m COM NEGATIVO AMARELO AZUL\033[m\n")

print("\033[32m SOMENTE LETRA VERDE \033[m\n")

print("\033[42m SOMENTE FUNDO VERDE \033[m\n")

print("\033[1m SOMENTE NEGRITO \033[m\n")

# METODO 1
A = 2
B = 7
print("\033[35mOs valores sao: \033[1;32m{}\033[35m e \033[1;31m{}\033[35m !!!\033[m\n".format(A, B))

# METODO 2
A = 2
B = 7
print("Os valores sao: {}{}{} e {}{}{} !!!\n".format(
    "\033[1;32m", A, " \033[m", "\033[1;31m", B, "\033[m"))

# METODO 3
A = 2
B = 7

cores = {'padrao': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'negrito e roxo': '\033[1;35m'}

print("{}Os valores sao: {}{}{} e {}{}{} !!!{}\n".format(
    cores["negrito e roxo"], cores['verde'], A, cores["negrito e roxo"], cores["vermelho"], B, cores["negrito e roxo"], cores["padrao"]))

# colorido

co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[m'}
print('{}={}={}={}={}{}'.format(co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*30)

# 2 cores 
vm = '\033[1;31m'
az = '\033[1;36m'
vr = '\033[1;32m'
am = '\033[1;33m'
rx = '\033[1;35m'
ptb = '\033[1;30;107m'
pt = '\033[1;30m'
lp = '\033[m'

# LINHA BR
az = '\033[1;36m'
am = '\033[1;33m'
vr = '\033[1;32m'
lp = '\033[m'
print(f'{az}#{am}#{vr}#{lp}'*20)