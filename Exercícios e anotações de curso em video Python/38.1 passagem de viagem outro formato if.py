'''pergunte a distancia de uma viagem em KM. calcule o preço da passagem, cobrando R$0,50 por KM
para viagens ate 200KM e R$0,45 oara viagens mais longas'''

km = float(input("Digite a qnt de KM: "))

preco = km * 0.50 if km <= 200 else km * 0.45
print("o preço da passagem é {:.2f}R$".format(preco))
