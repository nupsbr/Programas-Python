# leia uma frase e mostre;
# qnts vezes aparece a letra"A"
# em q posição eka aparece a priveira vez
# em q posição ela aparece a ultima vez

fr = str(input("Digite alguma coisa: ")).strip().upper()
print(("A letra A aparece {} vezes!").format(fr.count('A')))
print("A primeira letra A apareceu na posição: {}".format(1+fr.find('A')))
print("A ultima letra A apareceu na posição: {}".format(1+fr.rfind('A')))
