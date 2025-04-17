# Programa de Consumo #

distancia = float(input("Digite o total de distância percorrida (em KM): "))
combustivel = float(input("Digite a quantidade de combustível gasto (em L): "))

consumo = distancia / combustivel

print(f"\nO consumo médio de combustivél para uma distância de {distancia}KM é de: {consumo:.3f}L p/ KM")