N = int(input())

def soma_dois(x, y):
    if x % 2 == 0:
        x = x + 1

    soma = x
    for i in range(y-1):
        x = x + 2
        soma = soma + x
    return soma

for i in range(N):
    x, y = map(int,input().split())
    resultado = soma_dois(x, y)
    print(resultado)

#     if x % 2 == 0: 
#         primeiro_impar = x + 1
#         lista =[primeiro_impar]
#         k = 2 
#         numero = 2
#         while k <= y:
#             variavel = primeiro_impar + numero
#             lista.append(variavel)
#             numero += 2
#             k += 1

#         print(sum(lista))

#     else:
#         lista =[x]
#         k = 2
#         numero = 2
#         while k <= y:
#             variavel = x + numero
#             lista.append(variavel)
#             numero += 2
#             k += 1

#         print(sum(lista))