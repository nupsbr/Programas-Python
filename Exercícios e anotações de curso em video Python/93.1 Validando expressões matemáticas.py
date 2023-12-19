expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:  # qnd formar um par de () ele deleta da pilha e continua, mas qnd o par nao for formado ele da break
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # remove o ultimo val da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:  # se a pilha nao tiver nada ESTA CORRETA
    print('Sua expressao esta CORRETA!')
else:
    print('Sua expressao esta ERRADA!')
