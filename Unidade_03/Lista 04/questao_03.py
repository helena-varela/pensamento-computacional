N = int(input("Digite o valor de N: "))

def valido(numero):
    if N >= 1:
        return True

def piramide_de_numeros(numero):
    if valido(numero):
        for i in range(N+1):
            for j in range(i):
                print(i, end=" ")

            print()
    else:
        print("Valor inválido!")

piramide_de_numeros(N)