'''Leia dois numeros inteiro e compre-os mostrando na tela uma mensagem: 
o primeiro valor é maior:
o segundo valor e maior:
nao existe valor maior os dois sao iguar
'''
import emoji
from time import sleep


n = int(input(emoji.emojize("\033[1;36mDigite o 1️⃣   °  numero:")))
n2 = int(input(emoji.emojize("Digite o 2️⃣    °  numero: ")))
print("CARREGANDO...")
sleep(2)
if n > n2:
    print(emoji.emojize('O1️⃣ °  numero é maior  🥳'))
elif n < n2:
    print(emoji.emojize("O2️⃣ °  numero é maior  🥳"))
else:
    print(emoji.emojize(
        "\t\033[4;33m⚠️ ⚠️ ⚠️ ⚠️  NÃO EXISTE NUMERO, OS DOIS SÃO IGUAIS ⚠️ ⚠️ ⚠️ ⚠️\033[m"))
