'''leia o sexo de uma pessoa, mas só aceita os valores M ou F.
caso esteja errado peça a digitação novamente ate ter um valor correto'''
r = ''
while r != str('M') and r != str('F'):
    r = str(input('Digite seu sexo[M/F]: '))
    while r != str('M') and r != str('F'):
        r = str(input('TEM QUE SER [M] OU [F]: '))
print('FIM')
