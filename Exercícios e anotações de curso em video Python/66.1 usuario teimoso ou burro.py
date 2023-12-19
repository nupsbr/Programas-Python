'''leia o sexo de uma pessoa, mas só aceita os valores M ou F.
caso esteja errado peça a digitação novamente ate ter um valor correto'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))