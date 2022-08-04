a = str(input('Qual é o seu nome? '))
b = int(input('Qual a sua idade? '))
c = str(input('Seu nome é {}, e voce tem {} anos, certo?'.format(a, b)))
if c == 'sim':
    print('Muito bem, guardamos sua resposta!')
else:
    print('Que pena, reescreva seus dados e tente novamente!')
