N = int(input("Quantos alunos? "))

nomes = []
print("Digite os nomes dos alunos: ")

for i in range(N):
    nome = input()
    nomes.append(nome)

pares = nomes[1::2]
inverte = pares[::-1]
nomes[1::2] = inverte
print("\nNova lista: ")
for i in nomes:
    print(i.capitalize())