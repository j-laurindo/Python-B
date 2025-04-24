print("--- ARREMESSO DE DARDO ---")
print("> Informe as distâncias de cada chance de lançamento de dardo que você teve e descubra qual foi a maior distância")

distancia1 = float(input("Digite o valor da primeira distância: "))
distancia2 = float(input("Digite o valor da segunda distância: "))
distancia3 = float(input("Digite o valor da terceira distância: "))

if distancia1 > distancia2 and distancia1 > distancia3:
    print(f"\n> A maior distância foi na primeira tentativa, de {distancia1:.1f}m")
elif distancia2 > distancia1 and distancia2 > distancia3:
    print(f"\n> A maior distância foi na segunda tentativa, de {distancia2:.1f}m")
else:
    print(f"\n> A maior distância foi na terceira tentativa, de {distancia3:.1f}m")

