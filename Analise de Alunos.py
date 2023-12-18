import csv
lista2 = list()
with open('dados.csv', 'r', newline='\n') as arq:
    texto = csv.reader(arq)
    lista = list(texto)

 
for el in lista[1:]:
    dici = {
        'Nome': el[0],
        'Idade': int(el[1]),
        'Diciplina': el[2],
        'Nota1': el[3],
        'Nota2': el[4],
        'Media_nota': (float(el[3]) + float(el[4]))/2
    }
    lista2.append(dici.copy())
  
#print(lista2)


lista_disciplinas = [a['Diciplina'] for a in lista2]  # Lista com todas as disciplinas
contagem_disciplinas = {}  # Dicionário para manter a contagem de cada disciplina

# Contagem da frequência de cada disciplina
for i in lista_disciplinas:
    if i not in contagem_disciplinas:
        contagem_disciplinas[i] = 1
    else:
        contagem_disciplinas[i] += 1

# Encontrar a disciplina mais comum
disciplina_mais_comum = max(contagem_disciplinas, key=contagem_disciplinas.get)

# Nome dos alunos com a media maior ou igual a 7
cont = 0
print('Os alunos que tiveram a media maior ou igual a 7 foram:', end=' ')
for i in lista2:
    if i['Media_nota'] >= 7:
        print(i['Nome'], end=", ")
        cont += 1
print(f'\nO total de alunos que tiveram a media maior ou igual a 7 fora: {cont}')

# Media de idades de todos os alunos
print('A media das idades de todos os alunos são: ', end='')
media_idade = 0
qnt = 0
for i in lista2:
    media_idade += i['Idade']
    qnt += 1
  
print(f'{media_idade/qnt:.3}')

# Printa a disciplina mais comum
print(f'A disciplina mais comum é "{disciplina_mais_comum}"')

# Media e Nome de todos os alunos
media_aluno = [[el['Nome'], el['Media_nota']] for el in lista2]
print(f'\nMédias de todos os alunos: {media_aluno} ')


