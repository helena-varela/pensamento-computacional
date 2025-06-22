N = int(input("Qual o valor de N? "))

def eh_primo(numero):
    contador = 0
    lista = []
    for i in range(1, numero+1):
        if numero % i == 0:
            lista.append(i)
            contador += 1

    if contador == 2:
        print(f"{numero} é primo")
    else: 
        print(f"{numero} não é primo, os divisores são: {lista}")

print("Digite os valores: ")
numeros = []
for i in range(N):
    numero = int(input())
    numeros.append(numero)

print("\nA classificação é: ")
for i in numeros:
    eh_primo(i)