a = (1, 2, 3)
b = (4, 5, 6, 7, 3)
c = a + b
d = b + a

print(c)
print(d)
print(len(c))  # tamanho d c
print(c.count(3))  # qnt 3 existe em c        = 2
print(c.index(4))  # em que posicao esta o 4      = 3
print(c.index(3, 3))  # mostre o 3 apartir da posicao 3   = 7

pessoa = ('Higor', 22, 'M', 'Maluco')
print(pessoa)
del(pessoa) #apaga a tupla inteira