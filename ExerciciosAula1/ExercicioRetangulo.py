# Programa do retângulo #

# Importa biblioteca math
import math

# Solicita o usuário os valores
largura = float(input("Digite o valor da largura do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))

# Calculo da área de do valor
area = largura * altura
perimetro = 2 * (largura + altura)
diagonal = math.sqrt(math.pow(largura, 2) + math.pow(altura, 2))

# Exibe os calculos para o usuário
print(f"\nA área do retângulo é de: {area:.4f}m²")
print(f"O perímetro do retângulo é de: {perimetro:.4f}m")
print(f"A diagonal do retângulo é de: {diagonal:.4f}m")