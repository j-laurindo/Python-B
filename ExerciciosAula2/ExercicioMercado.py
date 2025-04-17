# Cria uma função de menu de escolha, que atribui toda a lógica para dentro dele
def menu():
    print("-> Escolha um mercado <-")
    print("1. São Vicente")
    print("2. PagueMenos")

    escolha = input("Digite o número do mercado desejado: ")

    # Lógica da escolha do mercado
    if escolha == '1':
        print(f"\n-> Você escolheu o São Vicente")
    elif escolha == '2':
        print("\n-> Você escolheu o PagueMenos")
    else:
        print("Opção Inválida")

    # Lógica para os itens
    if escolha == '1':
        qtd = int(input("\nDigite a quantidade de itens: "))
        item = float(input("Digite o preco do item: "))
        preco = qtd * item
        print(f"\n-> PREÇO DO ITEM ESCOLHIDO: {item:.2f} \n-> PREÇO TOTAL: {preco:.2f}", end="\n -- Obrigado pela preferência, volte sempre! --\n")
    if escolha == '2':
        qtd = int(input("\nDigite a quantidade de itens: "))
        item = float(input("Digite o preco do item: "))
        preco = qtd * (item * 2)
        print(f"\n-> PREÇO DO ITEM ESCOLHIDO: {item:.2f} \n-> PREÇO TOTAL: {preco:.2f}", end="\n -- Obrigado pela preferência, volte sempre! --\n")

# Função "menu" sendo chamada
menu()