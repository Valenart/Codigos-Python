import math
CA = float(input('Escreva o valor do Cateto Adjacente: '))
CO = float(input('Escreva o valor do Cateto Oposto: '))
Hipotenusa = (CA**2 + CO**2)
Raiz = math.sqrt(Hipotenusa)
print('O valor da hipotenusa será de {:.2f}'.format(Raiz))
