quilometro = float(input("Qual é a distância da viagem de ida e volta em quilômetros? "))
kmlitro = float(input("Quantos quilômetros o carro percorre com cada litro de combustível? "))
preco = float(input("Qual é o preço em reais por litro de combustível? "))

kms = quilometro / kmlitro
valor = kms * preco

print(f"O valor em reais para realizar a viagem pretendida é {valor: .2f}")