from random import shuffle

n1 = str(input('Qual é o Primeiro aluno? '))
n2 = str(input('Qual é o Segundo aluno? '))
n3 = str(input('Qual é o Terceiro aluno? '))
n4 = str(input('Qual é o Quarto aluno? '))
Lista = [n1, n2, n3, n4]
shuffle(Lista)
print('A ordem dos alunos será: ')
print(Lista)