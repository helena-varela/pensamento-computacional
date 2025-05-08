altura_levi = float(input("Altura inicial de Levi: "))
taxalevi = int(input("Taxa de crescimento de Levi: "))
altura_hiago = float(input("Altura inicial de Hiago: "))
taxahiago = int(input("Taxa de crescimento de Hiago:"))

taxahiagometros = taxahiago / 100
taxalevimetros = taxalevi / 100

if altura_hiago > altura_levi and taxalevi > taxahiago:
    anos = 0
    while altura_levi <= altura_hiago:
        altura_hiago = altura_hiago + taxahiagometros
        altura_levi = altura_levi + taxalevimetros
        anos += 1
    
    print("Serão necessários " + str(anos) + " anos para que Levi seja maior que Hiago.")
elif altura_hiago < altura_levi:
    print("Erro: Hiago deve ser maior que Levi inicialmente.")
elif taxalevi < taxahiago:
    print("Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.")
