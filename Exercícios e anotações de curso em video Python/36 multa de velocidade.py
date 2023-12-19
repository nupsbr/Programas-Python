# leia a velocidade de um carro se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado
# a multa vai custar R$7,00 por cada km acima do limite

import emoji
from time import sleep

print('='*50)
print("LIMITE DE VELOCIDADE: 80KM/H ")
print('='*50)
print('\n')

lm = float(input("Qual foi a velocidade do carro: "))
print('\n')
print("PROCESSANDO...")
sleep(3)
print(emoji.emojize("DADOS PROCESSADOS COM SUCESSO!!😀\n"))
sleep(2)
if lm <= 80:
    print(emoji.emojize(
        "O CARRO ESTA NO LIMITE DE VELOCIDADE!! :polegar_para_cima:", language='pt'))
else:
    lm = lm - 80
    res = lm * 7
    print(emoji.emojize(
        "O CARRO PASSOU DOS LIMITES DE VELOCIDADE!!:polegar_para_baixo:", language='pt'))
    print("A multa é do valor de: {}R$".format(res))
