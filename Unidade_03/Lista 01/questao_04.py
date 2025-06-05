coordenadas = input()
a, b, c, d, e, f = map(int,coordenadas.split())

if (a <= e <= c) and (b <= f <= d):
    print("Dentro!")
else:
    print("Fora!")