# Programa de Medidas #

# Solicitou os valores para o usuário
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Calculo das áreas
area_quadrado = A * A
area_triangulo = (A * B) / 2
area_trapezio = ((A +  B) * C) / 2

# Exibe respostados valores de cada área
print(f"\n-> ÁREA DO QUADRADO (Lado = {A}) = {area_quadrado:.4f}")
print(f"-> ÁREA DO TRIÂNGULO (Base = {A} e Altura = {B}) = {area_triangulo:.4f}")
print(f"-> ÁREA DO TRAPÉZIO (Bases = {A}, {B} e Altura = {C}) = {area_quadrado:.4f}")