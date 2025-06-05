temperatura = input()
numero, unidade = temperatura.split()
numero = float(numero)

if unidade == "F":
    celsius = ((numero - 32) * 5)/9
    kelvin = celsius + 273.15
    print("Temperatura em Celsius: %.2f°C " %celsius, "Temperatura em Fahrenheit: %.2f°F" %numero, "Temperatura em Kelvin: %.2fK" %kelvin )
elif unidade == "K":
    celsius = numero - 273.15
    fahrenheit = ((celsius * 9) + 160)/5
    print("Temperatura em Celsius: %.2f°C " %celsius, "Temperatura em Fahrenheit: %.2f°F" %fahrenheit, "Temperatura em Kelvin: %.2fK" %numero )
else:
    fahrenheit = ((numero * 9) + 160)/5
    kelvin = numero + 273.15
    print("Temperatura em Celsius: %.2f°C " %numero, "Temperatura em Fahrenheit: %.2f°F" %fahrenheit, "Temperatura em Kelvin: %.2fK" %kelvin )