"""leia o salario do funcionario e calcule o valor do seu aumento, para slarios superiores a: 
R$1.250,00, calcule o aumento de 10% e para inferiores ou iguais o aumento é de 15%."""

import emoji
from time import sleep
print('=-'*50)
sal = float(input("Digite o salario do funcionario: "))
print('=-'*50)
print(emoji.emojize("\n\t⏳ ESTAMOS PROCESSANDO POR FAVOR AGUARDE! 🙃"))
sleep(3)
print(emoji.emojize("\t⌛ DADOS PROCESSADOS COM SUCESSO!\n 😎👍"))
sleep(2)

if sal <= 1250:
    print("O aumento do salario R${:.2f} e de 15%' e ficaria com: R${:.2f} 💲🤑\n\n".format(
        sal, sal/100*15+sal))
else:
    print("O aumento do salario R${:.2f} é de 10%' e ficaria com: R${:.2f} 💸💰\n\n".format(
        sal, sal/100*10+sal))
