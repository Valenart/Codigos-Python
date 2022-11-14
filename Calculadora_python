import math
print('\033[34m==============TESTE DE CALCULADORA PYTHON==============\033[m')
print('\033[34m1\033[m = Soma \n\033[34m2\033[m = Subtração \n\033[34m3\033[m = Multiplicação ')
print('\033[34m4\033[m = Divisão')
print('\033[34m5\033[m = Seno,cosseno e tangente de um ângulo \n\033[34m6\033[m = Potencia')
print('\033[34m7\033[m = Hipotenusa \n\033[34m8\033[m = Conversor de Temperatura')
decisao = int(input('\n\033[4;34mOlá, qual será o tipo de conta que voce precisa fazer hoje?\033[m '))

# Soma
if decisao == 1:
    soma_decisao1 = float(input('Qual será o primeiro número a ser somado? '))
    soma_decisao2 = float(input('Qual será o segundo Número? '))
    soma_resultado = (soma_decisao1 + soma_decisao2)
    print('O valor da soma entre {:.2f} + {:.2f} será de {:.2f}'.format(soma_decisao1, soma_decisao2, soma_resultado))

# Subtração
elif decisao == 2:
    sub_decisao1 = float(input('Qual será o número minuendo? '))
    sub_decisao2 = float(input('Qual será o número que irá subtrair? '))
    sub_resultado = (sub_decisao1 - sub_decisao2)
    print('O valor da subtração entre {:.2f} - {:.2f} será de {:.2f}'.format(sub_decisao1, sub_decisao2, sub_resultado))

# Multiplicação
elif decisao == 3:
    mul_decisao1 = int(input('Qual será o número a ser multiplicado? '))
    mul_decisao2 = int(input('Qual será o multiplicador? '))
    mul_resultado = (mul_decisao1 * mul_decisao2)
    print('O valor da multiplicação entre {} x {} será de {:.0f}'.format(mul_decisao1, mul_decisao2, mul_resultado))

# Divisão
elif decisao == 4:
    div_decisao1 = int(input('Qual será o número divisor? '))
    div_decisao2 = int(input('Qual será o número dividendo? '))
    res_div = input('Quer saber qual é o resto da divisão?'.upper())
    div_resultado = (div_decisao1 / div_decisao2)
    print('O valor da divisão entre {} / {} será de {:.0f}'.format(div_decisao1, div_decisao2, div_resultado))
    if res_div == 'SIM':
        div_resultado2 = (div_decisao1 % div_decisao2)
        print('O resto da divisão é {}'.format(div_resultado2))

# Seno, Cosseno e Tangente de um angulo
elif decisao == 5:
    angulo_decisao = float(input('Qual ângulo voce deseja calcular? '))
    Seno = math.sin(math.radians(angulo_decisao))
    Cosseno = math.cos(math.radians(angulo_decisao))
    Tangente = math.tan(math.radians(angulo_decisao))
    print('O Seno do angulo {:.0f}° é {:.2f} '.format(angulo_decisao, Seno))
    print('O Cosseno do angulo {:.0f}° é {:.2f} '.format(angulo_decisao, Cosseno))
    print('A Tangente do angulo {:.0f}° é {:.2f} '.format(angulo_decisao, Tangente))

# Potencia
elif decisao == 6:
    potencia = int(input('Qual será o valor da base? '))
    potencia2 = int(input('Qual será o valor da potencia (expoente)? '))
    potencia_total = (potencia ** potencia2)
    print('O valor será de {}'.format(potencia_total))

# Hipotenusa
elif decisao == 7:
    CA = float(input('Escreva o valor do Cateto Adjacente: '))
    CO = float(input('Escreva o valor do Cateto Oposto: '))
    Hipotenusa = (CA ** 2 + CO ** 2)
    Raiz = math.sqrt(Hipotenusa)
    print('O valor da hipotenusa será de {:.2f}'.format(Raiz))

# Compliquei o código um pouco nessa parte da Temperatura
elif decisao == 8:
    print('\033[32m1\033[m = Celsius \n\033[32m2\033[m = Fahrenheit \n\033[32m3\033[m = Kelvin')
    temp1 = int(input('\033[4;32mQual será a medida a ser convertida?\033[m '))

    # Se a primeira medida for Celsius
    if temp1 == 1:
        print('\033[33m1\033[m = Fahrenheit \n\033[33m2\033[m = Kelvin')
        temp1_2 = int(input('\033[33mQual é a segunda medida conversora?\033[m '))
        if temp1_2 == 1:
            cels1_1 = float(input('Informe a temperatura em °C: '))
            cels_fahr = ((cels1_1 * 1.8) + 32)
            print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(cels1_1, cels_fahr))
        elif temp1_2 == 2:
            cels1_2 = float(input('Informe a temperatura em °C: '))
            cels_kel = (cels1_2 + 273.15)
            print('A temperatura de {:.1f}°C corresponde a {:.2f}°K!'.format(cels1_2, cels_kel))
        else:
            print('\033[7;44mErro! responda somente com 1 ou 2!\033[m')

    # Se a primeira medida for Farenheit
    elif temp1 == 2:
        print('\033[33m1\033[m = Celsius \n\033[33m2\033[m = Kelvin')
        temp1_2 = int(input('Qual é a segunda medida conversora? '))
        if temp1_2 == 1:
            fahr1_1 = float(input('Informe a temperatura em °F: '))
            fahr_cels = ((fahr1_1 - 32)/1.8)
            print('A temperatura de {:.1f}°F corresponde a {:.1f}°C!'.format(fahr1_1, fahr_cels))
        elif temp1_2 == 2:
            fahr1_2 = float(input('Informe a temperatura em °F: '))
            fahr_kel = ((fahr1_2 - 32)/1.8)+273.15
            print('A temperatura de {:.1f}°F corresponde a {:.2f}°K!'.format(fahr1_2, fahr_kel))
        else:
            print('\033[7;44mErro! responda somente com 1 ou 2!\033[m')

    # Se a primeira medida for Kelvin
    elif temp1 == 3:
        print('\033[33m1\033[m = Celsius \n\033[33m2\033[m = Fahrenheit')
        temp1_2 = int(input('Qual é a segunda medida conversora? '))
        if temp1_2 == 1:
            kel1_1 = float(input('Informe a temperatura em °K: '))
            kel_cels = (kel1_1 - 273.15)
            print('A temperatura de {:.2f}°K corresponde a {:.1f}°C!'.format(kel1_1, kel_cels))
        elif temp1_2 == 2:
            kel1_2 = float(input('Informe a temperatura em °K: '))
            kel_fahr = ((kel1_2 - 273.15) * 1.8)+32
            print('A temperatura de {:.2f}°K corresponde a {:.2f}°F!'.format(kel1_2, kel_fahr))
        else:
            print('\033[7;44mErro! responda somente com 1 ou 2!\033[m')

    else:
        print('\033[7;44mErro! responda somente de 1 até 3!\033[m')

else:
    print('\033[7;44mPor favor,digite um número de 1 a 8!\033[m')
