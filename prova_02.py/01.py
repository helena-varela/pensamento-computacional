idade = int(input())

if idade >= 16 and idade < 18:
    print("Tem idade para votar\nNão tem idade para dirigir")
elif idade < 16:
    print("Não tem idade para votar\nNão tem idade para dirigir")
elif idade >= 18:
    print("Tem idade para votar\nTem idade para dirigir")