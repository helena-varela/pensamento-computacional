N = int(input("Digite um valor: "))

def inverte(numero):
    numero = list(str(numero))
    numero = numero[::-1]
    valor=''
    for i in numero:
        valor += i 
    return valor

print(inverte(N))