frase = 'curso em video python'
print(frase)
print(frase[3])
print(frase[3:14])
print(frase[3:14:2])
print(frase[:14])
print(frase[::2])
print(frase.count('o'))  # conta qnts letra "o" tem na frase
print(len(frase))  # qual o tamanho da frase!!!!
print(len(frase.strip()))  # tamanho da frase em espaços
print(frase.replace('python', 'java'))  # troca uma palavra por outra
print('curso' in frase)  # palavra dentro da frase true ou false
print(frase.find('video'))  # mostra a posicao da palavra
print(frase.split())  # divide a frase em listas

print('\n\n')
# escrever texto grande em 1 print (usa 3 " )
print("""Essa receita de bolo é uma daquelas receitas básicas e deliciosas: ele pode ser incrementado com calda de chocolate, 
recheio de brigadeiro, doce de leite e outras delícias.
A sua dúvida é como fazer um bolo fofinho e molhadinho para a sobremesa?
Separamos 10 dicas muito fáceis e úteis. Com certeza você vai fazer sucesso, 
não importa se com uma receita de bolo comum ou bem elaborado.""")
