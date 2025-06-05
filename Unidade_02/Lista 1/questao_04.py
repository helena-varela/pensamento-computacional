numero = int(input("Qual é o número inteiro que deve ser utilizado para gerar a sequência? "))

numero1 = numero - 1
numero2 = numero1 - 1
numero3 = numero + 1
numero4 = numero3 + 1
total = numero + numero1 + numero2 + numero3 + numero4

print("A sequência é a seguinte:", str(numero2) + " " + str(numero1) + " " + str(numero) + " " + str(numero3) + " " + str(numero4) + " " + str(total))