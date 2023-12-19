'''Leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status de acordo com a tabela abaixo:
abaixo de 18.5 = ABAIXO DO PESO
entre 18.5 a 25 = PESO IDEAL
25 ate 30 = SOBREPESO
30 ate 40 = OBESIDADE
acima 40 = OBESIDADE MORBIDA

calculo:  imc = peso / (altura ** 2)'''
peso = float(input("Informe seu PESO: "))
altura = float(input("Informe sua ALTURA: "))


imc = peso / (altura ** 2)

print(f"Seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc < 40:
    print("OBESIDADE")
elif imc >= 40:
    print("OBESIDADE MORBIDA")
