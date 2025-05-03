peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc > 30.0:
    print("Obesidade")