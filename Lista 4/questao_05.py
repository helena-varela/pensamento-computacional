lista = []
while True:
    numeros = int(input("Informe as pontuações dos atletas. Digite -1 para encerrar. "))
    if numeros == -1:
        break
    else:
        lista.append(numeros)

maior = max(lista)
print("O recorde de pontos é " + str(maior))