lista= []
print("Digite 10 números: ")

for i in range(10):
    numeros = int(input())
    lista.append(numeros)

soma = sum(lista)
media = soma/10
print("A média é: " + str(media))
print("Os números acima da média são:")
for j in lista:
    if j > media:
        print(j)