nome = input("Nome: ")
idade = int(input("Idade: "))

if idade < 5:
    print("Categoria não aplicável para menores de 5 anos.")
elif idade <= 5 and idade <= 10:
    print("O atleta " + nome + " está classificado na categoria Infantil.")
elif idade >= 11 and idade <= 15:
    print("O atleta " + nome + " está classificado na categoria Juvenil")
elif idade >= 16 and idade <= 20:
    print("O atleta " + nome + " está classificado na categoria Júnior.")
elif idade >= 20 and idade <= 25:
    print("O atleta " + nome + " está classificado na categoria Profissional")
elif idade > 25:
    print("Fora das categorias estabelecidas.")