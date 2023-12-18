'''Calcule o valor a ser pago por um produto
considere o seu preço normal e condição de pagamento:

- A vista DINHEIR/CHEQUE:        10% de desconto
- Em ate 2X NO CARTAO:           preço normal
- 3X OU MAIS no cartao:          20% de juros
- a vista no CARTAO:             5% de desconto
'''
from time import sleep
co = {'1': '\033[31m', '2': '\033[32m', '3': '\033[33m',
      '4': '\033[34m', '5': '\033[35m', 'pad': '\033[m'}
print('{}={}={}={}={}{}'.format(
    co['1'], co['2'], co['3'], co['4'], co['5'], co['pad'],)*10)
print(f"{co['2']}======SISTEMA DE PAGAMENTO=======\n")
c = float(input("Informe o valor da compra: "))
sleep(1)
print("POR FAVOR AGUARDE!")
sleep(2)
while True:  # INICIA / ONDE VOLTA CASO ESCOLHA ERRADO
    print('''\n\tEscolha um Metodo de pagamento:
          
1 - A vista DINHEIRO/CHEQUE; 
2 - 2x no CARTÃO;
3 - 3x ou mais no CARTÃO
4 - A vista no CARTÃO\n''')

    es = int(input("Metodo de pagamento: "))
    print("PROCESSANDO")
    sleep(1)
    if es == 1:
        print(f'''\nA VISTA EM  DINHEIRO/CHEQUE:\nO valor total R${c:.2f} a vista em dinheiro/cheque é R${ c - c*10/100:.2f} {co['pad']}''')
        break
    elif es == 2:
        print(f'''\n2X NO CARTÃO:\nO valor da compra em 2x no CARTÃO é R${c:.2f}{co['pad']}''')
        break
    elif es == 3:
        while True:  # INICIA / ONDE VOLTA CASO ESCOLHA ERRADO
            p = int(input('Quantidades de parcelas: '))
            if p < 3 or p > 20:
                print("PORFAVOR INSIRA NO MINIMO 3 PARCELAS E NO MAXIMO 20 PARCELAS\n")
                continue
            else:
                total = c + (c * 20/100)
                parcela = total / p
                print(f'''\n Sua compra sera parcelada em {p}x de R${parcela:.2f} COM JUROS\nSua compra de R${c:.2f} vai custar R${total:.2f} ao todo.{co['pad']}''')
                break
        break
    elif es == 4:
        print(f'''\nA VISTA NO CARTÃO:\nO valor total R${c:.2f} a vista CARTÃO é R${ c - c*5/100:.2f} {co['pad']}''')
        break
    else:  # vai voltar no primeiro while pq n tem break
        print("Digite o numero de 1 a 4 para seu metodo de pagamento!\n\n")
        sleep(2)
