'''melhore o "PA while", perguntando para o usuario se ele que mostrar mais alguns termos.
o programa encerra enquando ele disse que quer mostrar 0 TERMOS'''
print("="*35)
print("\t10 TERMOS DE UMA PA")
print("="*35)
primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("razao: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais:'))
print('Progressa finalizada com {} termos mostrados'.format(total))