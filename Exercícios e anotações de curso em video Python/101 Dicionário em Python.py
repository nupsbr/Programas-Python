'''leia nome e media de um aluno, guardando a situação em um dicionario. No final, mostre o conteudo da
estrutura na tela'''

aluno = {'Nome': input('Nome: '), 'Média': float(input('Média: '))}
if aluno["Média"] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno["Média"] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('+-'*30)
for k, v in aluno.items():
    print(f'-   {k} é igual a {v}')
