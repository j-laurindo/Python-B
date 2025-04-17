import math

print("--- CALCULADORA DE FÓRMULA DE BHASKARA --\n")
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("\n-> Essa equação não tem raízes reais, portanto, não tem como realizar a fórmula de bhaskara")
    print(delta)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    if delta == 0:
        print("\n-> Essa equação possui somente uma raíz")
        print(f"-> RAÍZ = {raiz1} e {raiz2}")
    else:
        print("\n-- RAÍZES: --")
        print(f"-> X1 = {raiz1:.4f}")
        print(f"-> X2 = {raiz2:.4f}")


