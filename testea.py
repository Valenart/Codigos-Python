import math
A = float(input('Primeiro número: '))
B = float(input('Segundo número: '))
Hipotenusa = (A**2 + B**2)
Raiz = math.sqrt(Hipotenusa)
print('O valor da hipotenusa será de {:.2f}'.format(Raiz))
