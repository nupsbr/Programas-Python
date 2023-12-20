
vm = '\033[1;31m'
az = '\033[1;36m'
vr = '\033[1;32m'
am = '\033[1;33m'
rx = '\033[1;35m'
ptb = '\033[1;30;107m'
pt = '\033[1;30m'
br = '\033[1;37m'
brs = '\033[1;37;4m'
lp = '\033[m'


def liBR(n):  # linha cor br
    print(f'{az}▒{am}▒{vr}▒{lp}'*n)

def lirgb(n):
    print(f'{az}={vr}={vm}={lp}'*20)



def livm(n):  # linha vermelha
    print(f'{vm}={lp}'*n)


def livr(n):  # linha verde
    print(f'{vr}={lp}'*n)


def liaz(n):  # linha azul
    print(f'{az}={lp}'*n)


def liam(n):  # linha amarela
    print(f'{am}={lp}'*n)


def lirx(n):  # linha roxa
    print(f'{rx}={lp}'*n)
