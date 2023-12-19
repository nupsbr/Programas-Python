'''Mostre a tabuada de arios num, um de cada v ez, para cada valor digitado pelo usuario.
o programa sera interrompido qnd o num solicitado for negativo'''
az = '\033[1;36m'
vr = '\033[1;32m'
vm = '\033[1;31m'
pt = '\033[1;30m'
am = '\033[1;33m'
rx = '\033[1;35m'
lp = '\033[m'
print(f'{pt}-------------------\n{rx}TABUADA IMFINITA{pt}\n-------------------{lp}')
while True:
    n = int(input(
        f'Quer ver a tabuada de qual valor: \n{pt}Numeros negativos encerra o programa!{lp}'))
    if n < 0:
        print(f'{vm}PROGRAMA TABUADA ENCERRADO. volte sempre!{lp}')
        break
    for i in range(0, 11):
        print(f"{vr}{n} {pt}X {az}{i}{pt} = {am}{n*i}{lp}")
