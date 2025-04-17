print("--- CALCULE O PLANO CARTESIANO ---\n")

# Entrada de dados
x = float(input("Insira o valor de X: "))
y = float(input("Insira o valor de Y: "))

# Lógica do Exercício
if x == 0 and y == 0:
    print("A coordenada está na origem")
elif x == 0 and (y > 0 or y < 0):
    print("Eixo Y")
elif y == 0 and (x > 0 or x < 0):
    print("Eixo X")
elif x > 0 and y > 0:
    print("A coordenada está no quadrante Q1")
elif x < 0 and y > 0:
    print("A coordenada está no quadrante Q2")
elif x < 0 and y < 0:
    print("A coordenada está no quadrante Q3")
else:
    print("A coordenada está no quadrante Q4")