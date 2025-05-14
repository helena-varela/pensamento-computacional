qntpessoas = int(input("Qual o número de pessoas? "))

idades = []
for i in range(qntpessoas):
    idade = int(input("Informe as idades: "))
    idades.append(idade)

soma = sum(idades)
media = soma / qntpessoas
print("A média de idade das pessoas é " + str(media) + " anos")