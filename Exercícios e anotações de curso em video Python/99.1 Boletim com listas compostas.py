boletim = list()
while True:
    nome = str(input('Nome:')).upper()
    nota1 = float(input('Primeira Nota:'))
    nota2 = float(input('Segunda Nota:'))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('ERRO/ Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for pos, aluno in enumerate(boletim):
    print(f'ALUNO {pos}: {aluno[0]} / MÉDIA {aluno[2]}')
while True:
    opc = int(input('Quer mostrar a nota de qual aluno ? [999 PARA PARAR]'))
    for posi, notas in enumerate(boletim):
        if opc == posi:
            print(f'A notas de {notas[0]} é igual a {notas[1]}')
    if opc == 999:
        break