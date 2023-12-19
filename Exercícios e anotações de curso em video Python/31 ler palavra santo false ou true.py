#ler o nome de uma ciade e diga se começa com o nome "SANTO"
cid = str(input("Qual o nome da sua cidade?")).strip()

print('{}'.format('SANTO' in cid.upper()))