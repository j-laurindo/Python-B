print("--- DESCUBRA SE SÃO MÚLTIPLOS ---")
valor1 = int(input("\n-> Insira o primeiro valor: "))
valor2 = int(input("-> Insira o segundo valor: "))

if valor1 % valor2 == 0:
    if valor1 > valor2:
        print(f"{valor1} é múltiplo de {valor2}")
    else:
        print(f"{valor2} é múltiplo de {valor1}")
elif valor2 % valor1 == 0:
    if valor1 > valor2:
        print(f"{valor1} é múltiplo de {valor2}")
    else:
        print(f"{valor2} é múltiplo de {valor1}")
else:
    print(f"{valor1} não é múltiplo de {valor2}")