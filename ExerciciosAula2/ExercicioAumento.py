def retornar():
    print("\n\n------------------------------------------------------------------------")
    print("                 -> Gostaria de retornar à calculadora?                 ")
    print("------------------------------------------------------------------------")
    print("                          S = Sim  |  N = Não                           ")
    print("------------------------------------------------------------------------")
    opcao = input("Digite sua resposta: ")

    if opcao == "S" or opcao == "s":
        menu_aumento()
        retornar()
    else:
        print("------------------------------------------------------------------------")
        print("               -> Obrigada pela preferência, volte sempre!              ")
        print("------------------------------------------------------------------------")


def menu_aumento():
    print("\n\n--- CALCULO DO AUMENTO PERCENTUAL ---")
    print("------------------------------------")
    print("SALÁRIO ATUAL    |    AUMENTO  ")
    print("------------------------------------")
    print("Até R$1000       |       20%   ")
    print("1000 até R$3000  |       15%   ")
    print("3000 até R$8000  |       10%   ")
    print("Acima de R$8000  |        5%   ")
    print("------------------------------------")

    nome = input("-> Digite o nome do funcionário: ")
    salario = float(input("-> Digite o salário atual desse funcionário: R$"))

    if salario <= 1000:
        aumento = (20 / 100) * salario
        novo_salario = aumento + salario
        print("------------------------------------")
        print(f"FUNCIONÁRIO   |  {nome}")
        print(f"NOVO SALÁRIO  |  R${novo_salario:.2f}")
        print(f"AUMENTO       |  R${aumento:.2f}")
        print(f"PORCENTAGEM   |  20%")
        print("------------------------------------")
    elif salario <= 3000:
        aumento = (15 / 100) * salario
        novo_salario = aumento + salario
        print("------------------------------------")
        print(f"FUNCIONÁRIO   |  {nome}")
        print(f"NOVO SALÁRIO  |  R${novo_salario:.2f}")
        print(f"AUMENTO       |  R${aumento:.2f}")
        print(f"PORCENTAGEM   |  15%")
        print("------------------------------------")
    elif salario <= 8000:
        aumento = (10 / 100) * salario
        novo_salario = aumento + salario
        print("------------------------------------")
        print(f"FUNCIONÁRIO   |  {nome}")
        print(f"NOVO SALÁRIO  |  R${novo_salario:.2f}")
        print(f"AUMENTO       |  R${aumento:.2f}")
        print(f"PORCENTAGEM   |  10%")
        print("------------------------------------")
    elif salario > 8000:
        aumento = (5 / 100) * salario
        novo_salario = aumento + salario
        print("------------------------------------")
        print(f"FUNCIONÁRIO   |  {nome}")
        print(f"NOVO SALÁRIO  |  R${novo_salario:.2f}")
        print(f"AUMENTO       |  R${aumento:.2f}")
        print(f"PORCENTAGEM   |  5%")
        print("------------------------------------")

menu_aumento()
retornar()