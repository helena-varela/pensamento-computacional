N = int(input("Qual o N? "))

lista = []
print("Digite os valores:")
for i in range(N):
	numeros = int(input())
	lista.append(numeros)
	
OP = int(input("Qual a OP? "))
A = int(input("Qual o A? "))
B = int(input("Qual o B? "))

if OP == 0:
	resposta = lista[A-1] + lista[B-1]
	print(f"{lista[A-1]} + {lista[B-1]} = {resposta}")
elif OP == 1:
	resposta = lista[A-1] * lista[B-1]
	print(f"{lista[A-1]} * {lista[B-1]} = {resposta}")