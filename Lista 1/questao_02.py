multa1 = float(input("Qual é o valor original cobrado por cada multa? "))
juros = float(input("Qual é a porcentagem de juros cobrada pelo Detran? "))
amigos = int(input("Quantos amigos irão contribuir com as despesas? "))

multatotal = multa1 * 2
porcentagem = juros / 100
valor = multatotal * porcentagem
totalcomjuros = multatotal + valor
resposta =  totalcomjuros / amigos

print(f'O valor em reais que cada amigo deverá pagar ao Detran é {resposta: .2f}')