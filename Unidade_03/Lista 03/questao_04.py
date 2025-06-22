N = int(input("Quantos nomes? "))

nomes = []
print("Digite o nome do aluno: ")
for i in range(N):
    nome = input()
    nomes.append(nome)

nomes = nomes[::-1]
print("\nVocê digitou: ")
for i in nomes:
    print(i.capitalize())