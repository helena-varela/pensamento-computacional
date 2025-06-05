notas = []

for i in range(10):
    numeros = int(input("Digite 10 números: "))
    notas.append(numeros)

soma = sum(notas)
media = soma/10
print("A média é: " + str(media))
print("Os números acima da média são:")
for j in notas:
    if j > media:
        print(j)