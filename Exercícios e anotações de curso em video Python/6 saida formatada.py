print('='*30)  # imprime 30 vezes o =
nome = input('Digite seu nome: ')

print('='*50)
# adiciona nome dentro do print
print('Ola, seja Bem-Vindo: {} !!!'.format(nome))
print('='*50)
print('Ola, seja Bem-Vindo: {:20} !!!'.format(nome))  # 20 caracteres
print('='*50)
print('Ola, seja Bem-Vindo: {:>20} !!!'.format(nome))  # 20 pra direita >
print('='*50)
print('Ola, seja Bem-Vindo: {:<20} !!!'.format(nome))  # 20 pra esquerda <
print('='*50)
print('Ola, seja Bem-Vindo: {:^20} !!!'.format(nome))  # meio do 20
print('='*50)
print('Ola, seja Bem-Vindo: {:=^20} !!!'.format(nome))  # meio do 20 com =
print('='*50)
