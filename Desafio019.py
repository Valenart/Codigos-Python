import random
Primeiro = str(input('Qual o nome do Primeiro aluno? '))
Segundo = str(input('Qual o nome do Segundo aluno? '))
Terceiro = str(input('Qual o nome do Terceiro aluno? '))
Quarto = str(input('Qual o nome do Quarto aluno? '))
lista = [Primeiro, Segundo, Terceiro, Quarto]
Escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(Escolhido))
