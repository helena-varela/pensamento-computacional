meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

numero = int(input("Qual o número do mês? "))

if numero < 1 or numero > 12:
    print("Erro: não existe mês de número " + str(numero) + "! Por favor, digite um número entre 1 e 12")
else:
    mes = meses[numero - 1]
    print("O mês é " + mes)