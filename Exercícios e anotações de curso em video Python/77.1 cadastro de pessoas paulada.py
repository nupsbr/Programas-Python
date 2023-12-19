op=' '
ct=fct=mct=0
while op not in 'N':
    print('='*30)
    print('CADASTRE UMA PESSOA')
    print('='*30)
    id=int(input('Digite sua idade:'))
    se=str(input('Digite seu Sexo:(Masculino ou feminino)')).split()
    op=str(input('Digite (S/N) para continuar ou não o programa')).upper()
    cads=se[0][0].upper()
    if  id>18:
        ct+=1
    if cads == 'M':
        mct+=1
    if cads =='F' and id<20:
        fct+=1
print(f'Existem {ct} pessoas maiores de 18 anos')
print(f'Existem {mct} homens cadastrados')
print(f'Existem {fct}  mulheres com menos de 20 anos')