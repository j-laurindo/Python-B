def retornar():
    print("\n\n--- Gostaria de utilizar o programa mais uma vez? ---")
    print("S = Sim  |  N = Não")
    resp = input("\n> Digite sua resposta: ")

    if resp == "S" or resp == "s":
        menu_lanchonete()
        retornar()
    else:
        print("\n-- Obrigado, volte sempre! --\n")

def menu_lanchonete():
    print("\n\n-- CAIXA DE PRODUTOS DA LANCHONETE --")
    print("Informe qual é o código do produto e calcule o valor total de sua compra ")
    print("\n-------------------------------")
    print("CÓDIGO D/ PRODUTO |  PREÇO")
    print("-------------------------------")
    print("        1         |  R$5,00 ")
    print("        2         |  R$3,50 ")
    print("        3         |  R$4,80 ")
    print("        4         |  R$8,90 ")
    print("        5         |  R$7,32 ")
    print("-------------------------------")

    produto = int(input("\n> Digite o código do produto: "))

    if produto == 1:
        print("\nCÓDIGO ESCOLHIDO: 1  |  PREÇO: R$5,00")
        qtd = int(input("> Digite a quantidade de produtos: "))
        total = 5 * qtd
        print(f"\nQUANTIDADE DE PRODUTOS: {qtd}  |  VALOR TOTAL: R${total:.2f}")
    elif produto == 2:
        print("\nCÓDIGO ESCOLHIDO: 2  |  PREÇO: R$3,50")
        qtd = int(input("> Digite a quantidade de produtos: "))
        total = 3.50 * qtd
        print(f"\nQUANTIDADE DE PRODUTOS: {qtd}  |  VALOR TOTAL: R${total:.2f}")
    elif produto == 3:
        print("\nCÓDIGO ESCOLHIDO: 3  |  PREÇO: R$4,80")
        qtd = int(input("> Digite a quantidade de produtos: "))
        total = 4.80 * qtd
        print(f"\nQUANTIDADE DE PRODUTOS: {qtd}  |  VALOR TOTAL: R${total:.2f}")
    elif produto == 4:
        print("\nCÓDIGO ESCOLHIDO: 4  |  PREÇO: R$8,90")
        qtd = int(input("> Digite a quantidade de produtos: "))
        total = 8.90 * qtd
        print(f"\nQUANTIDADE DE PRODUTOS: {qtd}  |  VALOR TOTAL: R${total:.2f}")
    elif produto == 5:
        print("\nCÓDIGO ESCOLHIDO: 5  |  PREÇO: R$7,32")
        qtd = int(input("> Digite a quantidade de produtos: "))
        total = 7.32 * qtd
        print(f"\nQUANTIDADE DE PRODUTOS: {qtd}  |  VALOR TOTAL: R${total:.2f}")
    else:
        print("\nOPÇÃO INVÁLIDA")


menu_lanchonete()
retornar()

