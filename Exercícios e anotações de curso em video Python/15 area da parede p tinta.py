# leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2 m^2
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: \n'))

print('Sua parede tem a dimensão de {} x {} e a sua area é de {}m2.'.format(l, a, l*a))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(l*a/2))
