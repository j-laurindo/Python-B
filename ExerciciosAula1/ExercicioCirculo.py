# Programa Área do Círculo #

# Importa a biblioteca Math
import math
print("\n-- CALCULE A ÁREA DO RAIO --\n")

# Solicita as infromações para o usuário
raio = float(input("Digite o raio do círculo: "))

# Calcula a area do círculo
area = 3.14159 * math.pow(raio,2)

# Exibe o resultado para o usuário
print(f"\n-> A área do círculo com o raio {raio} é: {area:.3f}")