# faça com que o computador "pense" em um numero inteiro entre 0e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhifo pela maquina. o programa devera escrever na tela se o usuario venceu ou perdeu
import random
from time import sleep
import emoji

print('='*50)
print("A divinhe se o numero entre 0 a 5 !!!")
print('='*50)
n = int(input("Escolha um numero inteiro que acha que a maquina escolheu: "))
print("PROCESSANDO...")
sleep(3)  # espera 3 seg
al = random.randint(0, 5)
print("NUMERO GERADO!!\n")
sleep(2)
if n == al:
    print(emoji.demojize("VOCE ACERTOU!!! :polegar_para_cima:", language='pt'))
else:
    print(emoji.emojize("VOCE ERROU!! :polegar_para_baixo:", language='pt'))
    print("O numero era: {}!".format(al))
