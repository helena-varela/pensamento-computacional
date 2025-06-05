qntpessoas = int(input("Qual o número de pessoas? "))

soma = 0
for i in range(qntpessoas):
    idades = int(input("Informe as idades: "))
    soma = soma + idades

media = soma / qntpessoas
print("A média de idade das pessoas é " + str(media) + " anos")