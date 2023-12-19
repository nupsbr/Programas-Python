'''Escreva um programa para aprovar o emprestimo bancario para a compra
de uma casa. Pergunte o VALOR DA CASA, o SALARIO do comprador
e em QUANTOS ANOS ele vai pagar.
A prestação mensal, nao pode exceder 30% do salario ou entao o emprestimo sera negado!'''

import emoji
from time import sleep
print("\033[1;34;43m=-"*40)
print(emoji.emojize('\n\t 💵 BEM-VINDO AO BANCO DO BRASIL!🌎 \n'))
casa = float(
    input(emoji.emojize('  💰🏡      Porfavor informe o VALOR DA CASA: ')))
sal = float(input(emoji.emojize("  🤑💳        Informe o SALARIO do COMPRADOR: ")))
ano = int(input(emoji.emojize("  😎📅           Quantos ANOS pretende pagar: ")))
print('\n')
print("PROCESSANDO...\n")
sleep(3)
print("CARREGANDO DADOS...\n")
sleep(2)
print("\033[1;31;43mERRO AO CARREGAR DADOS...👎😢\033[1;34;43m\n")
sleep(4)
print("PROCESSANDO...\n")
sleep(3)
print("CARREGANDO DADOS...\n")
sleep(3)
print(emoji.emojize(
    "\033[1;32mDADOS CARREGADOS COM SUCESSO! 😎👍\033[1;34;43m\n"))

prestacao = casa / (ano * 12)
sal30 = sal*30/100

cor = {'pad': '\033[0;1;34;43m',
       'val': '\033[4;32;43m'}

print("Para pagar uma casa de R${}{:.2f}{} em {}{}{} anos a prestação sera de R${}{:.2f}{} !!\n".format(
    cor['val'], casa, cor['pad'], cor['val'], ano, cor['pad'], cor['val'], prestacao, cor['pad']))
if prestacao > sal30:
    print(emoji.emojize("\033[1;31m\t❌EMPRESTIMO NEGADO❌ 👎😭\033[1;34;43m\n\n"))
else:
    print(emoji.emojize(
        "\033[1;32m\t✅EMPRESTIMO APROVADO✅ 🤑💰\033[1;34;43m\n\n"))
