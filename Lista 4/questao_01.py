confirmados = ['Daniel', 'Aluizio', 'Isabel', 'Teles','Eduardo']
nome = input("Qual nome você quer verificar? ")

print("A lista contém os seguintes nomes:")
for c in confirmados:
    print(c)

if nome in confirmados:
    print("O nome " +  nome + " está na lista, acesso permitido!")
else:
    print("O nome " +  nome + " não está na lista, acesso negado!")
