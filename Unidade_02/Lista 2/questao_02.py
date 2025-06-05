valorcompra = float(input("Qual o valor da compra? "))
pagar = input("Como gostaria de pagar à vista(V) ou à prazo (P)? ")

if pagar == 'V' or pagar == 'v':
    desconto = valorcompra * 0.05
    totaldesc = valorcompra - desconto
    print("Valor à pagar " + str(totaldesc)) 
else:
    aumento = valorcompra * 0.08
    totalaumento = valorcompra + aumento
    parcelas = totalaumento / 3
    print("Valor à pagar: " + str(totalaumento))
    print("Parcela 1: " + str(parcelas))
    print("Parcela 2: " + str(parcelas))
    print("Parcela 3: " + str(parcelas))