larg1 = float(input("Qual a largura do lote 1? "))
comp1 = float(input("Qual o comprimento do lote 1? "))

larg2 = float(input("Qual a largura do lote 2? "))
comp2 = float(input("Qual o comprimento do lote 2? "))

larg3 = float(input("Qual a largura do lote 3? "))
comp3 = float(input("Qual o comprimento do lote 3? "))

larg4 = float(input("Qual a largura do lote 4? "))
comp4 = float(input("Qual o comprimento do lote 4? "))

area1 = larg1 * comp1
area2 = larg2 * comp2
area3 = larg3 * comp3
area4 = larg4 * comp4
areatotal = area1 + area2 + area3 + area4

print(f"A área total do terreno é {areatotal}")