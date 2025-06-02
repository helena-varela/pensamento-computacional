quantidade_itens = int(input())

total = 0
for i in range(quantidade_itens):
    valor_item = float(input())
    qunt_por_item = int(input())
    total += qunt_por_item * valor_item

print("%.2f" % total)