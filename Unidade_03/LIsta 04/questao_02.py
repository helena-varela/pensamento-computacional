def eh_par(numero):
    lista = []
    for i in numero:
        if i % 2 == 0:
            lista.append(i)

    return print(f"Soma dos números pares: {sum(lista)}")

numeros = []
for i in range(4):
    numero = int(input(f"Digite número {i+1}: "))
    numeros.append(numero)

eh_par(numeros)