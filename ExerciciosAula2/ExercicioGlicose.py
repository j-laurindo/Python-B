print("--- DESCUBRA O SEU NÍVEL DE GLISOSE ---")
glic = int(input("Digite a quantidade de glicose no seu sangue: "))

if glic <= 100:
    print(f"\n> GLICOSE = {glic}mg/dl")
    print("> CLASSIFICAÇÃO: Nível Normal")
elif glic <= 140:
    print(f"\n> GLICOSE = {glic}mg/dl")
    print("> CLASSIFICAÇÃO: Nível Elevado")
else:
    print(f"\n> GLICOSE = {glic}mg/dl")
    print("> CLASSIFICAÇÃO: Nível Diabetes")