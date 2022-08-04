import math
Angulo = float(input('Qual angulo voce deseja calcular? '))
Seno = math.sin(math.radians(Angulo))
Cosseno = math.cos(math.radians(Angulo))
Tangente = math.tan(math.radians(Angulo))
print('O Seno do angulo {:.0f}° é {:.2f} '.format(Angulo, Seno))
print('O Cosseno do angulo {:.0f}° é {:.2f} '.format(Angulo, Cosseno))
print('A Tangente do angulo {:.0f}° é {:.2f} '.format(Angulo, Tangente))
