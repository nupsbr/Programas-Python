# pergunte a quantidade de KM percorrido pelo carro alugado e a
# quantidade de DIAS que foi alugado. Calcule o preço sabendo que o carro custa R$60 a diaria e R$ 0.15 por KM rodado

d = int(input('Quantos dias Alugados?: '))
k = float(input('Quantos KM rodados: '))

print('O total a pagar é de R${}'.format(d*60 + k * 0.15))
