gastos = []
while True:
    gasto = float(input("Informe os gastos no dia: "))
    if gasto == 0:
        break
    else:
        gastos.append(gasto)
 
if gastos:
    maximo = max(gastos)
    print("O seu maior gasto hoje foi R$ %.2f" %maximo)
else: 
    print("Você não teve gastos hoje!")