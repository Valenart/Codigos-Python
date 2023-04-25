n1 = input('Qual é o seu nome? ')
n2 = float(input('Qual é o seu peso? '))
n3 = float(input('qual a sua idade? '))
n4 = int(input('o dia do seu aniversário é: '))
n5 = input('Seu nome é {}, seu peso {},sua idade é {},dia do seu aniversário é dia {} correto? '.format(n1, n2, n3, n4))
if n5 == 'sim':
    print('Ah, que bom! O código está correto! =)')
else:
    print('Ah, que pena, vou melhorar! =(')
