#CRIE UM PROGRAMA QUE MOSTRE O MAIOR VALOR DENTRO DE UM ARRAY COM 5 POSIÇÕES USANDO O FOR

nomes = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]
valores = [0] * 5
i = 0
maior = 0

for i in range(5):
  valores[i] = (int(input("Escreva o {} número: ".format(nomes[i]))))
  if (maior < valores[i]):
    maior = valores[i]

print("O maior valor dentro do array será: ", maior)
