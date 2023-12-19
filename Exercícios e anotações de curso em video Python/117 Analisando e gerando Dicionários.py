def notas(*n, sit=False):
    """Funcao para analisar notas de varios alunos

    Args:
        n = uma ou mais notas dos alunos (aceita varias)
        sit = mostra a situação da media do aluno
    Returns:
        dicionario com varias informaçoes sobre a situacao da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situacao'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situacao'] = 'RAZOAVEL'
        else:
            r['Situacao'] = 'RUIM'
    return r


# programa

resp = notas(5.4, 3.5, 7, 8.6, sit=True)
print(resp)

resp = notas(5.4, 3.5, 7, 8.6)
print(resp)

help(notas)