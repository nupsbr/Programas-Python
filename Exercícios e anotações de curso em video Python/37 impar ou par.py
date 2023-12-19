#leia um numero inteiro e mostre se ele é impar ou par

n = int(input("Digite um numero:  "))

res= n %2

if res == 0:
    print("PAR")
else:
    print("IMPAR")