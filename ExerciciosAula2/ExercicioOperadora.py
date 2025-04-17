print("--- VERIFICADOR DE CONSUMO TELEFÔNICO ---\n")
minutos = int(input("Digite a quantidade de minutos consumidos: "))
valor = 50

if minutos <= 100:
    print(f"\n-> Minutos Consumidos: {minutos}")
    print(f"-> Preço: R${valor:.2f}")
else:
    minutos_add = minutos - 100
    preco = valor + (minutos_add * 2)
    print(f"\n-> Minutos Consumidos: {minutos} min")
    print(f"-> Preço: R${preco:.2f}")

