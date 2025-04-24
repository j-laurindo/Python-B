
print("--- MENOR ENTRE TRÊS NÚMEROS ---\n")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if num1 < num2 and num1 < num3:
    print(f"\n-> Maiores números: {num2} e {num3}")
    print(f"-> {num1} é o menor valor")
elif num2 < num1 and num2 < num3:
    print(f"\n-> Maiores números: {num1} e {num3}")
    print(f"-> {num2} é o menor valor")
elif num3 < num1 and num3 < num2:
    print(f"\n-> Maiores números: {num1} e {num2}")
    print(f"-> {num3} é o menor valor")
elif (num1 < num2 and num1 == num3) or (num1 < num3 and num1 == num2):
    print(f"\n-> {num1} é o menor número")
elif (num2 < num1 and num2 == num3) or (num2 < num3 and num2 == num1):
    print(f"\n-> {num2} é o menor número")
elif (num3 < num1 and num3 == num2) or (num3 < num2 and num3 == num1):
    print(f"\n-> {num3} é o menor número")
else:
    print("\n-> Todos os números são iguais")