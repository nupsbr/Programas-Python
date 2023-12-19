'''pergunte a distancia de uma viagem em KM. calcule o preço da passagem, cobrando R$0,50 por KM
para viagens ate 200KM e R$0,45 oara viagens mais longas'''

km = float(input("Digite a qnt de KM: "))

if km <= 200:
    print("o preço da passagem é {:.2f}R$".format(km*0.50))
else:
    print("o preço da passagem com disconto é de {:.2f}R$".format(km*0.45))
