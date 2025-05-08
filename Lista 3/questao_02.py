taxas = []
for i in range(10):
    taxa = int(input("Insira a taxa do exame para 10 pacientes: "))
    taxas.append(taxa)

soma_arit = 0
for j in taxas:
    soma_arit = soma_arit + j

media_aritmetica = soma_arit/10

inverter = 0
for k in taxas:
    inverter += 1/k

media = inverter/10
media_harmonica = 1/media

produto = 1
for l in taxas:
    produto = produto * l

media_geometrica = produto ** (1/10)

erro_harmonico = (media_harmonica - media_aritmetica)/media_aritmetica
erro_geometrica = (media_geometrica - media_aritmetica)/media_aritmetica
erro_medio = (erro_harmonico + erro_geometrica)/2
porcentagem = erro_medio * 100

print("Média Aritmética: %.2f" % media_aritmetica)
print("Média Harmônica: %.2f" % media_harmonica)
print("Média Geométrica: %.2f" % media_geometrica)
print("Erro médio: %.2f%%" % porcentagem) 