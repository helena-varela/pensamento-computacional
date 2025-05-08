cachorro_quente = 0
bauru = 0
hamburguer = 0
cheeseburguer = 0
refrigerante = 0
while True:
    item = int(input("Digite o código do item: "))
    if item == -1:
        break
    quantidade = int(input("Digite a quantidade: "))
    if item == 100:
        cachorro_quente = 5.50 * quantidade 
    elif item == 101:
        bauru = 15 * quantidade
    elif item == 103:
        hamburguer = 20 * quantidade
    elif item == 104:
        cheeseburguer = 18 * quantidade
    elif item == 105:
        refrigerante = 6 * quantidade

total = cachorro_quente + bauru + hamburguer + cheeseburguer + refrigerante
print("Total a pagar: R$ %.2f" % total)
