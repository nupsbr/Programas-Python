'''Leia i comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo'''
import emoji

print('=-'*20)
s1 = float(input("📐Digite o primeiro seguimento: "))
print('=-'*20)
s2 = float(input("📐Digite o segundo seguimento: "))
print('=-'*20)
s3 = float(input("📐Digite o terceiro seguimento: "))
print('=-'*20)

somas2s3 = s2 + s3
somas1s3 = s1 + s3
somas1s2 = s1 + s2

if s1 >= somas2s3:
    print(emoji.emojize(
        "\nNao da pra fazer um triangulo s1 é maior q soma s2 + s3 = {} 😔🔺\n".format(somas2s3)))

elif s2 >= somas1s3:
    print(emoji.emojize(
        "\nNao da pra fazer um triangulo s2 é maior q soma s1 + s3 = {} 😔🔺\n".format(somas1s3)))

elif s3 >= somas1s2:
    print(emoji.emojize(
        "\nNao da pra fazer um triangulo s3 é maior q soma s1 + s2 = {} 😔🔺\n".format(somas1s2)))

else:
    print("\n😎👍\tDA PRA FAZER UM TRIANGULO!! 🔺{} 🔺{} 🔺{} \n\n".format(
        somas2s3, somas1s3, somas1s2))
