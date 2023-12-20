from Pacote_uteis import c 

def menu():
    c.liam(50),print(f'\t\t{c.az}MENU PRINCIPAL'),c.liam(50)


def menuCP():
    {c.liam(50),print(f'\t\t{c.az}MENU PRINCIPAL'),c.liam(50),
        print(f'{c.az}1{c.lp} - {c.br}Ver pessoas cadastradas.'),print(f'{c.az}2{c.lp} - {c.br}Cadastrar nova Pessoa.'),
        print(f'{c.az}3{c.lp} - {c.br}Sair do Sistema'),c.liam(50)}

def continuar():
    sn = str(input(f'{c.br}Deseja continuar? [{c.vr}S{c.br}/{c.vm}N{c.br}] ')).strip().upper()[0]
    while sn not in 'SsNn':
        sn= str(input(f'{c.vm}Dados inválidos. Deseja continuar?{c.br} [{c.vr}S{c.br}/{c.vm}N{c.br}]: ')).strip().upper()[0]

def continuarMN():
    sn = str(input(f'{c.br}Deseja voltar ao MENU PRINCIPAL? [{c.vr}S{c.br}] ')).strip().upper()[0]
    while sn not in 'Ss':
        sn= str(input(f'{c.vm}Dados inválidos. Deseja voltar ao MENU PRINCIPAL?{c.br} [{c.vr}S{c.br}]: ')).strip().upper()[0]

