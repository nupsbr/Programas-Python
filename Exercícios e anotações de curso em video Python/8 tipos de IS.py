n = input('Digite algo ou um valor:  ')

print('é numerico?        ==', n.isnumeric())  # é numerico?
print('é do alfabeto?     ==', n.isalpha())  # é alfabeto?
print('é alfanumerico?    ==', n.isalnum())  # é alfanumerico?
print('esta em maiusculo? ==', n.isupper())  # é somente em maiusculo?
print('esta em minusculo? ==', n.islower())  # é somente em minusculo?
print('é um espaço?       ==', n.isspace())  # é somente um espaço?
print('é um digito?       ==', n.isdigit())  # é um digito?
print('é um titulo?       ==', n.istitle())  # sera true se tiver MAIUSCULO?
print('é um caractere?    ==', n.isascii())  # é um caractere?
print('é imprimivel?      ==', n.isprintable())  # da pra imprimir?
