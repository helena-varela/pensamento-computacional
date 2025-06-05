numero = int(input("Digite um número: "))
if numero <= 0:
    print("O número deve ser maior que 0.")
else:
    produto = 1
    for i in range(1, numero + 1):
        produto *= i
        
    print("Resultado do fatorial: " + str(produto))