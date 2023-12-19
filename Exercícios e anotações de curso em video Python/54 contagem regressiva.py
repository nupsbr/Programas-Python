'''contagem regressiva de 10 ate 0 com pausa de 1 seg'''
from time import sleep
for cont in range(10, -1, -1):  # coloca -1 mostrar o 0
    print(cont)
    sleep(1)
print("acabou!!!!")
