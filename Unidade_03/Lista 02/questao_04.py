T = int(input())
for i in range(T):
    PA, PB, G1, G2 = map(float, input().split())
    PA = int(PA)
    PB = int(PB)
    
    anos = 0
    G1 = G1/100
    G2 = G2/100
    while PA <= PB:
        if anos > 100:
            break
        else:
            PA += int(PA * G1)
            PB += int(PB * G2)
            anos += 1
    
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(str(anos), "anos.")