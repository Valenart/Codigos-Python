alt = float(input('Qual é a altura da parede em metros? '))
lar = float(input('E a largura? (metros também) '))
mul = (alt * lar)
div = (mul / 2)
print('para pintar uma parede de {} m², voce precisará de {} litros de tinta.'.format(mul, div))

