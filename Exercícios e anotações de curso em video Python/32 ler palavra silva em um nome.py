# ler o nome e diga se tem "silva" no nome
import emoji
nome = str(input("Qual o seu nome?: ")).strip()

nome = ('SILVA' in nome.upper())

if nome == False:
    print(emoji.emojize("FALSO :polegar_para_baixo:", language='pt'))
if nome == True:
    print(emoji.emojize("VERDADEIRO :polegar_para_cima:", language='pt'))
